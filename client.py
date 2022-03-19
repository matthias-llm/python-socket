from ast import Str
import sys, socket

from attr import define

# GET 	: html body + metainfo
# HEAD 	: metainfo
# PUT 	: ?
# POST 	: ?

class ClientSocket:
	BUFFERSIZE = 4096

	command = ""
	uri = ""
	port = 0

	soc = 0
	ip = ""

	request = ""
	response = ""

	charset = "ISO-8859-1"
	filetype = ""

	def input_commands(self, command, uri, port):
		self.command = command
		self.uri = uri
		self.port = int(port)

	def create_socket(self):
		try:
			self.ip = socket.gethostbyname(self.uri)
			self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# AF_INET = ipv4; SOCK_STREAM = standaard protocol
		except socket.error as e:
			print(e)

	def connect_socket(self):
		try:
			self.soc.connect((self.ip, self.port))
		except socket.error as e:
			print(e)

	def close_connection(self):
		self.soc.shutdown(socket.SHUT_RDWR)
		self.soc.close()

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

	def retrieve_embedded_images(self):
		pass

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

		return file_type_1[:-1], file_type_2

	def check_page_length(self, header):
		substr_cl = "Content-Length: "
		substr_te = "Transfer-Encoding: chunked"

		content_length = header.find(substr_cl)
		transfer_format = header.find(substr_te)
		
		if transfer_format != -1:
			return -1
		elif content_length != -1:
			s = ""
			while header[content_length + len(substr_cl)] != "\r":
				s += header[content_length + len(substr_cl)]
				content_length += 1

			return int(s)

	def make_html_output(self):
		start_html = self.response.find("<!doctype html>")	#	Not always in html file

		if start_html == -1:
			start_html = self.response.find("<html>")		#	Always in html file, not plaintext

		if start_html == -1:
			substr = "\r\n\r\n"

			start_html = self.response.find(substr)		# 	Then it is plaintext

			self.response = self.response[start_html + len(substr):]
		else:
			self.response = self.response[start_html:]

	def remove_end(self):
		if self.filetype == "html":
			if "<HTML>" in self.response:
				substr = "</HTML>"
				end = self.response.find(substr)
				self.response = self.response[:(end+len(substr))]
			else:
				substr = "</html>"
				end = self.response.find(substr)
				self.response = self.response[:(end+len(substr))]

	def get_chunked(self, buffer):
		if self.filetype == "html":
			if "<HTML>" in buffer:
				while "</HTML>" not in buffer:
					self.response += buffer
					buffer = self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

				self.response += buffer
			else:
				while "</html>" not in buffer:
					self.response += buffer
					buffer = self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

				self.response += buffer
		else:
			self.response += buffer	# TODO: Hoe het einde dan weten? Is dit zelfs nodig?

	def get_whole(self, buffer, chunk):
		self.response += buffer

		if len(buffer) < chunk:
			buffer = self.soc.recv(chunk - self.BUFFERSIZE).decode(encoding=self.charset)
			self.response += buffer

	def get(self, command):
		self.request = command + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n\r\n"
		self.soc.send(self.request.encode())
		
		#	This call receives the header
		buffer = self.soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		self.check_charset(buffer)
		chunk = self.check_page_length(buffer)		#	If chunked: chunk = -1
		filetype_1, self.filetype = self.check_file_type(buffer)

		if chunk == -1:
			self.get_chunked(buffer)
		else:
			self.get_whole(buffer, chunk)

		self.retrieve_embedded_images()

		self.make_html_output()
		self.remove_end()

	def head(self, command):
		self.request = command + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n\r\n"
		self.soc.send(self.request.encode())

		self.response = self.soc.recv(4096).decode(encoding=self.charset)		# Mogelijks niet lang genoeg

	def post(self, command, path, length):
		self.request = command + " " + path + " HTTP/1.1\r\nHost: " + self.uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self.soc.send(self.request.encode())

	def put(self, command, path, length):
		self.request = command + " " + path + " / HTTP/1.1\r\nHost: " + self.uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self.soc.send(self.request.encode())

	def write_output(self):
		if self.filetype == "plain":
			self.filetype = "txt"

		fout = open("output." + self.filetype, "w")

		fout.write(self.response)
		fout.close()

	def __init__(self, command, uri, port):
		self.input_commands(command, uri, port)
		self.create_socket()
		self.connect_socket()

		self.req(self.command)
		self.write_output()

		self.close_connection()


client = ClientSocket(sys.argv[1], sys.argv[2], sys.argv[3])