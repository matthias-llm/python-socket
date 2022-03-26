import sys, socket, bs4, re
from embedded_objects import EmbeddedObjects

class ClientSocket:
	_embedded_obj = EmbeddedObjects()

	BUFFERSIZE = 1
	end_of_header = "\r\n\r\n"
	stop = "\r\n"
	end_chars = ["\"", "\'", "(", "="]

	_command = ""
	_uri = ""
	_port = 0

	_soc = 0
	_ip = ""

	_request = ""
	_response = ""

	charset = "ISO-8859-1"
	filetype = ""

	def input_commands(self, command, port):
		self._command = command
		self._port = int(port)

	def create_socket(self, uri=_uri):
		try:
			ip = socket.gethostbyname(uri)
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#	AF_INET = ipv4; SOCK_STREAM = TCP
			soc.settimeout(5)
		except socket.error as e:
			print(e)

		return ip, soc

	def connect_socket(self):
		try:
			self._soc.connect((self._ip, self._port))
		except socket.error as e:
			print(e)

	def close_connection(self, soc):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	def _req(self, command):
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
	def _check_charset(self, header):
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
	def _get_header(self):
		buffer = self._soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)
		
		while self.end_of_header not in buffer:
			buffer += self._soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

	"""
	
	"""
	def _get_chunked(self):
		def in_buffer(buffer):
			if len(buffer) > len(self.stop):
				if buffer[-len(self.stop):] == self.stop:
					return False

			return True

		def get_chunksize():
			buffer = ""
			while in_buffer(buffer):
				buffer += self._soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

			if buffer[:len(self.stop)] == self.stop:
				buffer = buffer[len(self.stop):]

			return int(buffer[:-len(self.stop)], base=16)

		size = get_chunksize()

		while size != 0:
			buffer = ""

			while len(buffer) < size:
				size_counter = size - len(buffer)
				buffer += self._soc.recv(size_counter).decode(encoding=self.charset)

			self._response += buffer
			size = get_chunksize()

	def _get_whole(self, chunk):
		while len(self._response) < chunk:
			self._response += self._soc.recv(chunk).decode(encoding=self.charset)

	def get(self, command):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())
		
		header = self._get_header()
		self._check_charset(header)
		chunk = self._embedded_obj._check_page_length(header)
		filetype_1, self.filetype = self._embedded_obj._check_file_type(header)

		if chunk == -1:
			self._get_chunked()
		else:
			self._get_whole(chunk)

		self._response = self._embedded_obj.retrieve_embedded_objects(self._response, self._soc, self._uri)

	def head(self, command):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())

		self._response = self._get_header()

	def post(self, command, path, length):
		self._request = command + " " + path + " HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self._soc.send(self._request.encode())

	def put(self, command, path, length):
		self._request = command + " " + path + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self._soc.send(self._request.encode())

	def write_output(self, name):
		if self.filetype == "plain":
			self.filetype = "txt"
			
		print(name + "." + self.filetype)
		fout = open(name + "." + self.filetype, "w")

		fout.write(self._response)
		fout.close()

	def __init__(self, command, uri, port):
		self.input_commands(command, port)
		self._uri = uri
		self._ip, self._soc = self.create_socket(self._uri)
		self.connect_socket()

		self._req(self._command)
		self.write_output(uri)

		self.close_connection(self._soc)


# client = ClientSocket(sys.argv[1], sys.argv[2], sys.argv[3])