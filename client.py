from ast import Str
from fileinput import filename
import sys, socket, bs4, re

class ClientSocket:
	BUFFERSIZE = 1
	end_of_header = "\r\n\r\n"
	stop = "\r\n"

	file_extensions = [".jpg", ".png", ".js", ".css", ".gif"]
	end_chars = ["\"", "\'", "(", "="]

	command = ""
	uri = ""
	port = 0

	soc = 0
	ip = ""

	request = ""
	response = ""

	charset = "ISO-8859-1"
	filetype = ""

	def input_commands(self, command, port):
		self.command = command
		self.port = int(port)

	def create_socket(self, uri=uri):
		try:
			ip = socket.gethostbyname(uri)
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#	AF_INET = ipv4; SOCK_STREAM = TCP
			# self.soc.setblocking(0)		#	Voor select() later, select.select([socket], [], [], 5); imort select
			soc.settimeout(5)
		except socket.error as e:
			print(e)

		return ip, soc

	def connect_socket(self):
		try:
			self.soc.connect((self.ip, self.port))
		except socket.error as e:
			print(e)

	def close_connection(self, soc):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	def req(self, command):
		length = 30

		if command == "HEAD":
			self.head(command)
		elif command == "GET":
			self.get(command)
		elif command == "POST":
			self.post(command, input(), length)
		elif command == "PUT":
			self.put(command, input() , length)

	"""
		Checks the charset in the header and sets the correct global charset.
		Standard charset is ISO-8859-1, decodes same as UTF-8 for unicode chars.
	"""
	def check_charset(self, header):
		substr = "charset="
		pos = header.find(substr)

		if pos != -1:
			pos += len(substr)

			d = header[pos]
			pos += 1
			while header[pos] != "\r":
				if header[pos] == "\"":
					break
				d += header[pos]
				pos += 1

			self.charset = d

	"""
		Checks filetypes for filenameing purposes and file extensions.
	"""
	def check_file_type(self, header):
		substr = "Content-Type: "
		pos = header.find(substr)

		file_type_1 = ""
		file_type_2 = ""
		while header[pos + len(substr)] != ";":
			if header[pos + len(substr)] == "\r":
				break 
			
			if len(file_type_1) != 0:
				if file_type_1[-1] != "/":
					file_type_1 += header[pos + len(substr)]
				else:
					file_type_2 += header[pos + len(substr)]
			else:
				file_type_1 += header[pos + len(substr)]

			pos += 1

		if file_type_2 == "javascript":
			file_type_2 = "js"

		return file_type_1[:-1], file_type_2

	"""
		Finds Content-length if not transferred in chuncks, returns -1 if chunked.
	"""
	def check_page_length(self, header):
		substr_cl = "Content-Length: "
		substr_te = "Transfer-Encoding: chunked"

		content_length = header.find(substr_cl)
		transfer_format = header.find(substr_te)
		
		if transfer_format != -1:
			return -1
		elif content_length != -1:
			length = ""
			while header[content_length + len(substr_cl)] != "\r":
				length += header[content_length + len(substr_cl)]
				content_length += 1

			return int(length)

	def retrieve_embedded_files(self):
		def make_uri(url):
			u = ""
			index = 0

			while url[index] != "/":
				u += url[index]
				index += 1
			
			return u, index

		soup = bs4.BeautifulSoup(self.response, 'html.parser')
		i = 0
		results = []
		for s in self.file_extensions:
			results.append(soup.find_all(string=re.compile(s), recursive=True))
			i += 1

		counter = 0
		image = b""
		working_response = self.response

		for s in self.file_extensions:
			index = 0

			while working_response[index:].find(s) != -1:
				org_index = working_response[index:].find(s) + len(s) - 1
				index = org_index

				if not ((ord(self.response[index+1]) >= 65 and  ord(self.response[index+1]) <= 90) or (ord(self.response[index+1]) >= 97 and  ord(self.response[index+1]) <= 122)):
					url = ""

					while self.response[index] not in self.end_chars:
						url = self.response[index] + url
						index -= 1

					header = ""
					if url[:2] == "//":
						site, i = make_uri(url[2:])

						ip, soc = self.create_socket(site)
						soc.connect((ip, self.port))

						header = self.get_file("GET", url[2+i:], site, soc)

						size = self.check_page_length(header)
						filetype_1, filetype_2 = self.check_file_type(header)
						image = self.get_image(size, soc)
					elif url[:8] == "https://":
						site, i = make_uri(url[8:])

						ip, soc = self.create_socket(site)
						soc.connect((ip, self.port))

						header = self.get_file("GET", url[2+i:], site, soc)

						size = self.check_page_length(header)
						filetype_1, filetype_2 = self.check_file_type(header)
						image = self.get_image(size, soc)
					else:
						header = self.get_file("GET", url, self.uri, self.soc)

						size = self.check_page_length(header)
						filetype_1, filetype_2 = self.check_file_type(header)
						image = self.get_image(size, self.soc)

					if url[:2] == "//":
						self.close_connection(soc)
					if url[:8] == "http://":
						self.close_connection(soc)

					filename = self.uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
					fout = open(filename, "wb")
					fout.write(image)
					fout.close()

					working_response, start = self.replace_in_html(filename, org_index)

					index = start + len(filename)

					counter += 1
	
	def replace_in_html(self, filename, index):
		def start_org_filepath():
			i = 0

			while self.response[index-i] not in self.end_chars:
				i += 1
				
			return index - i

		start = start_org_filepath()
		filename_x = ""
		for i in filename:
			filename_x += "x"

		sta_string = self.response[:start+1]
		end_string = self.response[index+1:]

		self.response = sta_string + filename + end_string
		working_response = sta_string + filename_x + end_string

		return working_response, start

	def get_image(self, size, socket):
		image = b""

		if size == -1:
			self.get_chunked()
		else:
			while len(image) < size:
				image += socket.recv(size)

		return image

	def get_file(self, command, url, uri=uri, soc=soc):
		self.request = command + " /" + url + " HTTP/1.1\r\nHost: " + uri + "\r\n\r\n"
		soc.send(self.request.encode())

		buffer = ""
		while self.end_of_header not in buffer:
			buffer += soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

	def get_header(self):
		buffer = self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)
		
		while self.end_of_header not in buffer:
			buffer += self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

	def get_chunked(self):
		def in_buffer(buffer):
			if len(buffer) > len(self.stop):
				if buffer[-len(self.stop):] == self.stop:
					return False

			return True

		def get_chunksize():
			buffer = ""
			while in_buffer(buffer):
				buffer += self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

			if buffer[:len(self.stop)] == self.stop:
				buffer = buffer[len(self.stop):]

			return int(buffer[:-len(self.stop)], base=16)

		size = get_chunksize()

		while size != 0:
			buffer = ""

			while len(buffer) < size:
				size_counter = size - len(buffer)
				buffer += self.soc.recv(size_counter).decode(encoding=self.charset)

			self.response += buffer
			size = get_chunksize()

	def get_whole(self, chunk):
		while len(self.response) < chunk:
			self.response += self.soc.recv(chunk).decode(encoding=self.charset)

	def get(self, command):
		self.request = command + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n\r\n"
		self.soc.send(self.request.encode())
		
		#	This call receives the header
		header = self.get_header()
		self.check_charset(header)
		chunk = self.check_page_length(header)		#	If chunked: chunk = -1
		filetype_1, self.filetype = self.check_file_type(header)

		if chunk == -1:
			self.get_chunked()
		else:
			self.get_whole(chunk)

		self.retrieve_embedded_files()

	def head(self, command):
		self.request = command + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n\r\n"
		self.soc.send(self.request.encode())

		self.response = self.get_header()

	def post(self, command, path, length):
		self.request = command + " " + path + " HTTP/1.1\r\nHost: " + self.uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self.soc.send(self.request.encode())

	def put(self, command, path, length):
		self.request = command + " " + path + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self.soc.send(self.request.encode())

	def write_output(self, name):
		if self.filetype == "plain":
			self.filetype = "txt"
			
		print(name + "." + self.filetype)
		fout = open(name + "." + self.filetype, "w")

		fout.write(self.response)
		fout.close()

	def __init__(self, command, uri, port):
		self.input_commands(command, port)
		self.uri = uri
		self.ip, self.soc = self.create_socket(self.uri)
		self.connect_socket()

		self.req(self.command)
		self.write_output(uri)

		self.close_connection(self.soc)


client = ClientSocket(sys.argv[1], sys.argv[2], sys.argv[3])