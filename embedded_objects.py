import socket
from typing import Tuple

class EmbeddedObjects:
	file_extensions = [".jpg", ".png", ".js", ".css", ".gif"]
	end_chars = ["\"", "\'", "(", "=", ")"]
	end_of_header = "\r\n\r\n"
	BUFFERSIZE = 1
	charset = "ISO-8859-1"

	_port = 80
	_response = ""

	def make_uri(self, url:str):
		u = ""
		index = 0

		while url[index] != "/":
			u += url[index]
			index += 1
	
		return u, index

	def _create_socket(self, uri:str) -> Tuple[str, socket.SocketKind]:
		try:
			ip = socket.gethostbyname(uri)
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(5)
		except socket.error as e:
			print(e)

		return ip, soc

	def _close_connection(self, soc:socket.SocketKind):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	def _get_header(self, command:str, url:str, uri:str, soc:socket.SocketKind) -> str:
		request = command + " /" + url + " HTTP/1.1\r\nHost: " + uri + "\r\n\r\n"
		soc.send(request.encode())

		buffer = ""
		while self.end_of_header not in buffer:
			buffer += soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

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
			if response[index + 1] in self.end_chars:
				return reconstructed_response[-extension_length:] == extension

		return False

	def retrieve_embedded_objects(self, response:str, soc:socket.SocketKind, uri:str) -> str:
		global extension_length, reconstructed_response

		counter = 0
		reconstructed_response = ""

		for index in range(len(response)):
			reconstructed_response += response[index]
			url = ""
			
			for extension in self.file_extensions:
				extension_length = len(extension)

				if self._has_object(extension, response, index):
					while response[index] not in self.end_chars:
						url = response[index] + url
						index -= 1

					filename = ""
					
					if url[:len("https://")] == "https://":
						filename = self._get_object_external(counter, url[len("https://"):], uri)
					elif url[:len("//")] == "//":
						filename = self._get_object_external(counter, url[len("//"):], uri)
					elif url[0] == "/":
						filename = self._get_object_normal(counter, url, uri, soc)
					else:
						break

					reconstructed_response = self._replace_in_html(reconstructed_response, filename, url)

					counter += 1

					break

		return reconstructed_response

	def _write_output(self, uri:str, filetype_1:str, filetype_2:str, obj:bytes, counter:str) -> str:
		filename = uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
		fout = open(filename, "wb")
		fout.write(obj)
		fout.close()

		return filename

	"""
		Retrieve header and body and write file to disk.
	"""
	def _get_object_normal(self, counter:str, url:str, uri:str, soc:socket.SocketKind) -> str:
		header = self._get_header("GET", url, uri, soc)
		size = self._check_page_length(header)
		filetype_1, filetype_2 = self._check_file_type(header)
		obj = self._get_object(size, soc)		

		return self._write_output(uri, filetype_1, filetype_2, obj, counter)

	"""
		Retrieve header and body and write file to disk.
	"""
	def _get_object_external(self, counter:str, url:str, uri:str) -> str:
		site, i = self.make_uri(url)

		ip, soc = self._create_socket(site)
		soc.connect((ip, self._port))

		header = self._get_header("GET", url[i:], site, soc)

		size = self._check_page_length(header)
		filetype_1, filetype_2 = self._check_file_type(header)
		obj = self._get_object(size, soc)

		self._close_connection(soc)
		return self._write_output(uri, filetype_1, filetype_2, obj, counter)

	"""
		Uses binary format for receiving and writing objects
	"""
	def _get_object(self, size:int, socket:socket.SocketKind) -> bytes:
		obj = b""

		if size == -1:
			self.get_chunked()
		else:
			while len(obj) < size:
				obj += socket.recv(size)

		return obj

	def _replace_in_html(self, response:str, filename:str, url:str) -> str:
		return response.replace(url, filename)

	def __init__(self):
		pass