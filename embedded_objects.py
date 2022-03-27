import socket
from typing import Tuple
from util import Util

class EmbeddedObjects:
	_util = Util()

	_port = 80
	_response = ""

	def make_uri(self, url:str):
		u = ""
		index = 0

		while url[index] != "/":
			u += url[index]
			index += 1
	
		return u, index

	def _close_connection(self, soc:socket.SocketKind):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	"""
		Checks filetypes for filenameing purposes and file extensions.
		";" and "\r" can both be a terminating substring in the header.
		filetype is of form "abcd/abcd" with right what type of file it is.
	"""
	def _check_file_type(self, header:str) -> Tuple[str,str]:
		substr = "Content-Type: "
		pos = header.find(substr)

		file_type_1 = ""
		file_type_2 = ""
		while header[pos + len(substr)] not in [";", "\r"]:			
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
		"\r" signals a line-end.
	"""
	def _check_page_length(self, header:str) -> int:
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

	def _has_object(self, extension:str, response:str, index:int) -> bool:
		global extension_length, reconstructed_response

		if index + 1 < len(response):
			if response[index + 1] in self._util.end_chars:
				return reconstructed_response[-extension_length:] == extension

		return False

	def retrieve_embedded_objects(self, response:str, soc:socket.SocketKind, uri:str) -> str:
		global extension_length, reconstructed_response

		counter = 0
		reconstructed_response = ""

		for index in range(len(response)):
			reconstructed_response += response[index]
			url = ""
			
			for extension in self._util.file_extensions:
				extension_length = len(extension)

				if self._has_object(extension, response, index):
					while response[index] not in self._util.end_chars:
						url = response[index] + url
						index -= 1

					filename = ""
					
					if url[:len("https://")] == "https://":
						filename = self._get_object_external(counter, url[len("https://"):], uri)
					elif url[:len("//")] == "//":
						filename = self._get_object_external(counter, url[len("//"):], uri)
					elif url[:len("http://")] == "http://":
						filename = self._get_object_external(counter, url[len("http://"):], uri)
					elif url[0] == "/":
						filename = self._get_object_normal(counter, url, uri, soc)
					else:
						break

					reconstructed_response = self._util.replace_in_html(reconstructed_response, filename, url)

					counter += 1

					break

		return reconstructed_response

	"""
		Retrieve header and body and write file to disk.
	"""
	def _get_object_normal(self, counter:str, url:str, uri:str, soc:socket.SocketKind) -> str:
		request = "GET" + " /" + url + " HTTP/1.1\r\nHost: " + uri + "\r\n\r\n"
		soc.send(request.encode())

		header = self._util.get_header(soc)
		size = self._check_page_length(header)
		filetype_1, filetype_2 = self._check_file_type(header)
		obj = self._get_object(size, soc)		

		return self._util.write_output(uri, filetype_1, filetype_2, obj, counter)

	"""
		Retrieve header and body and write file to disk.
	"""
	def _get_object_external(self, counter:str, url:str, uri:str) -> str:
		site, i = self.make_uri(url)

		ip, soc = self._util.create_socket(site)
		self._util.connect_socket(soc, ip, self._port)

		request = "GET" + " /" + url[i:] + " HTTP/1.1\r\nHost: " + uri + "\r\n\r\n"
		soc.send(request.encode())

		header = self._util.get_header(soc)

		size = self._check_page_length(header)
		filetype_1, filetype_2 = self._check_file_type(header)
		obj = self._get_object(size, soc)

		self._util.close_connection(soc)
		return self._util.write_output(uri, filetype_1, filetype_2, obj, counter)

	"""
		Uses binary format for receiving and writing objects
	"""
	def _get_object(self, size:int, soc:socket.SocketKind) -> bytes:
		obj = b""

		if size == -1:
			obj = self._get_chunked(soc, obj)
		else:
			while len(obj) < size:
				obj += soc.recv(size)

		return obj

	def _get_chunked(self, soc:socket.SocketKind, obj:bytes) -> bytes:
		def in_buffer(buffer:str) -> bool:
			if len(buffer) > len(self.stop):
				if buffer[-len(self.stop):] == self.stop:
					return False

			return True

		def get_chunksize() -> int:
			buffer = ""
			while in_buffer(buffer):
				buffer += soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

			if buffer[:len(self.stop)] == self.stop:
				buffer = buffer[len(self.stop):]

			return int(buffer[:-len(self.stop)], base=16)

		size = get_chunksize()

		while size != 0:
			buffer = b""

			while len(buffer) < size:
				size_counter = size - len(buffer)
				buffer += soc.recv(size_counter)

			obj += buffer
			size = get_chunksize()

		return obj

	def __init__(self):
		pass