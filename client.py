import sys, socket
from typing import Tuple
from embedded_objects import EmbeddedObjects
from util import Util

class ClientSocket:
	"""
		These are private members of the ClientSocket class and shouldn't be used outside this package.
	"""
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

	"""
		This definition sets the command and port for later (internal) use.

		Public member.
	"""
	def input_commands(self, command:str, port:str):
		self._command = command
		self._port = int(port)

	"""
		This definition is called when the server works with chuncks instead of sending "the whole" message at once.
		There are two internal functions for a cleaner experience.

		Every time the current buffer length is compared (smaller than) to the chunck size.
		While this inequility is True the next bytes of that chunck are retrieved. This goes for every chucnk.

		Private member.
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

	"""
		Takes the whole message util the last byte is received. 
		The definition decodes the message instantly, this makes searching for embedded files easier later on.

		Private member.
	"""
	def _get_whole(self, chunk:int):
		while len(self._response) < chunk:
			self._response += self._soc.recv(chunk).decode(encoding=self._util.charset)

	"""
		This definition constructs the minimum GET message and sends it to the server.
		Upon answer of the server, first the head is read, some information is also extracted for later use.
		After the head, the body of the message (if any) is read in chunck or as a whole and embedded objects are retrieved.

		Public member.
	"""
	def get(self, command:str):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())
		
		header = self._util.get_header(self._soc)

		if header != "HTTP/1.1 404 Not Found\r\n\r\n":
			self._util.check_charset(header)
			chunk = self._embedded_obj._check_page_length(header)
			self._filetype_1, self._filetype_2 = self._embedded_obj._check_file_type(header)

			if chunk == -1:
				self._get_chunked()
			else:
				self._get_whole(chunk)

			self._response = self._embedded_obj.retrieve_embedded_objects(self._response, self._soc, self._uri)

	"""
		Constructs the HEAD message, sends that message and receives de head.

		Public member.
	"""
	def head(self, command:str):
		self._request = command + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n\r\n"
		self._soc.send(self._request.encode())

		self._response = self._util.get_header(self._soc)

	"""
		This definition asks for input of content and path of the file on the server.
		It also sends the request.

		Public member.
	"""
	def post(self, command:str, path:str):
		print("Input the content: ")
		message = input()

		self._request = command + " " + path + " HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(len(message.encode('utf-8'))) + "\r\n\r\n" + message
		self._soc.send(self._request.encode())

	"""
		This definition asks for input of content and path of the file on the server.
		It also sends the request.

		Public member.
	"""
	def put(self, command:str, path:str):
		print("Input the content: ")
		message = input()

		self._request = command + " " + path + " / HTTP/1.1\r\nHost: " + self._uri + "\r\n" + "Content-Length: " + str(len(message.encode('utf-8'))) + "\r\n\r\n" + message
		self._soc.send(self._request.encode())

	"""
		Used for control flow.

		Private member.
	"""
	def _req(self, command:str):
		if command == "HEAD":
			self.head(command)
		elif command == "GET":
			self.get(command)
		elif command == "POST":
			print("Input the path: ")
			self.post(command, input())
		elif command == "PUT":
			print("Input the path: ")
			self.put(command, input())

	"""
		Initialises the client by reading commands and calling above functions.
		Disconnecting is done after each request is finished, stopping the program is done by typing DISCONNECT! _ _
	"""
	def __init__(self): #, command:str, uri:str, port:str):
		print("Give a telnet command. The GET and HEAD function are constructed and sent automatically.\nDisconecting is done as follows: DISCONNECT! _ _\n\n")
		command, uri, port = input().split(" ")

		self.input_commands(command, port)
		self._uri = uri
		self._ip, self._soc = self._util.create_socket(self._uri)
		self._util.connect_socket(self._soc, self._ip, self._port)

		while self._util._connected == True:
			self._req(self._command)
		
			_ = self._util.write_output(uri, self._filetype_1, self._filetype_2, self._response)

			self._util.close_connection(self._soc)

			try:
				command, uri, port = input().split(" ")
			except ValueError as e:
				print()

			if command == "DISCONNECT!":
				break

			self.input_commands(command, port)
			self._uri = uri
			self._ip, self._soc = self._util.create_socket(self._uri)
			self._util.connect_socket(self._soc, self._ip, self._port)

# client = ClientSocket(sys.argv[1], sys.argv[2], sys.argv[3])
# client = ClientSocket("GET", sys.argv[2], "80")
client = ClientSocket()