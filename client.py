import sys, socket
from typing import Tuple
from embedded_objects import EmbeddedObjects
from util import Util

class ClientSocket:
	_embedded_obj = EmbeddedObjects()
	_util = Util()

	_command = ""
	_uri = ""
	_port = 0

	_soc = 0
	_ip = ""

	_request = ""
	_response = ""

	_filetype_1 = ""
	_filetype_2 = ""

	def input_commands(self, command:str, port:str):
		self._command = command
		self._port = int(port)

	"""
	
	"""
	def _get_chunked(self):
		def in_buffer(buffer:str) -> bool:
			if len(buffer) > len(self._util.stop):
				if buffer[-len(self._util.stop):] == self._util.stop:
					return False

			return True

		def get_chunksize() -> int:
			buffer = ""
			while in_buffer(buffer):
				buffer += self._soc.recv(self._util.BUFFERSIZE).decode(encoding=self._util.charset)

			if buffer[:len(self._util.stop)] == self._util.stop:
				buffer = buffer[len(self._util.stop):]

			return int(buffer[:-len(self._util.stop)], base=16)

		size = get_chunksize()

		while size != 0:
			buffer = ""

			while len(buffer) < size:
				size_counter = size - len(buffer)
				buffer += self._soc.recv(size_counter).decode(encoding=self._util.charset)

			self._response += buffer
			size = get_chunksize()

	def _get_whole(self, chunk:int):
		while len(self._response) < chunk:
			self._response += self._soc.recv(chunk).decode(encoding=self._util.charset)

	def get(self, command:str):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())
		
		header = self._util.get_header(self._soc)
		self._util.check_charset(header)
		chunk = self._embedded_obj._check_page_length(header)
		self._filetype_1, self._filetype_2 = self._embedded_obj._check_file_type(header)

		if chunk == -1:
			self._get_chunked()
		else:
			self._get_whole(chunk)

		self._response = self._embedded_obj.retrieve_embedded_objects(self._response, self._soc, self._uri)

	def head(self, command:str):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())

		self._response = self._util.get_header(self._soc)

	def post(self, command:str, path:str, length:int):
		self._request = command + " " + path + " HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self._soc.send(self._request.encode())

	def put(self, command:str, path:str, length:int):
		self._request = command + " " + path + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(length) + "\r\n\r\n"
		self._soc.send(self._request.encode())

	def _req(self, command:str):
		length = 30

		if command == "HEAD":
			self.head(command)
		elif command == "GET":
			self.get(command)
		elif command == "POST":
			self.post(command, input(), length)
		elif command == "PUT":
			self.put(command, input() , length)

	def __init__(self, command:str, uri:str, port:str):
		self.input_commands(command, port)
		self._uri = uri
		self._ip, self._soc = self._util.create_socket(self._uri)
		self._util.connect_socket(self._soc, self._ip, self._port)

		self._req(self._command)
		
		_ = self._util.write_output(uri, self._filetype_1, self._filetype_2, self._response)

		self._util.close_connection(self._soc)


#client = ClientSocket(sys.argv[1], sys.argv[2], sys.argv[3])
client = ClientSocket("GET", sys.argv[2], "80")