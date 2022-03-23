import sys, socket, bs4, re
from embedded_objects import Embedded_Objects

class ClientSocket:
	embedded_obj = Embedded_Objects()

	BUFFERSIZE = 1
	end_of_header = "\r\n\r\n"
	stop = "\r\n"

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
		Receive each byte seperately (self.BUFFERSIZE) until self.end_of_header is found in buffer.
	"""
	def get_header(self):
		buffer = self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)
		
		while self.end_of_header not in buffer:
			buffer += self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

	"""
	
	"""
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
		
		header = self.get_header()
		self.check_charset(header)
		chunk = self.embedded_obj.check_page_length(header)
		filetype_1, self.filetype = self.embedded_obj.check_file_type(header)

		if chunk == -1:
			self.get_chunked()
		else:
			self.get_whole(chunk)

		self.embedded_obj.retrieve_embedded_objects(self.response, self.soc, self.uri)

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