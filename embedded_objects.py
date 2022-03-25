import socket

class Embedded_Objects:
	file_extensions = [".jpg", ".png", ".js", ".css", ".gif"]
	end_chars = ["\"", "\'", "(", "="]

	end_of_header = "\r\n\r\n"
	BUFFERSIZE = 1
	charset = "ISO-8859-1"

	response = ""

	def make_uri(self, url):
		u = ""
		index = 0

		while url[index] != "/":
			u += url[index]
			index += 1
	
		return u, index

	def __close_connection(self, soc):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	def __get_header(self, command, url, uri, soc):
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
	def check_file_type(self, header):
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

	def __has_object(self, extension):
		global extension_length, reconstructed_response

		return reconstructed_response[-extension_length:] == extension

	def retrieve_embedded_objects(self, response, soc, uri):
		counter = 0
		url = ""

		for index in range(len(response)):
			for extension in self.file_extensions:
				global extension_length, reconstructed_response

				extension_length = len(extension)

				if self.__has_object(extension):
					while response[index] not in self.end_chars:
						url = response[index] + url
						index -= 1

					filename = ""
					
					if url[:len("https://")] == "https://":
						filename = self.__get_object_external(counter, url, uri)
					elif url[:len("//")] == "//":
						filename = self.__get_object_external(counter, url, uri)
					else:
						filename = self.__get_object_normal(counter, url, uri, soc)

					self.replace_in_html(response, filename, url)

					counter += 1	

	"""
		Retrieve header and body and write file to disk.
	"""
	def __get_object_normal(self, counter, url, uri, soc) -> str:
		header = self.__get_header("GET", url, uri, soc)
		size = self.check_page_length(header)
		filetype_1, filetype_2 = self.check_file_type(header)
		obj = self.get_object(size, soc)		

		filename = uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
		fout = open(filename, "wb")
		fout.write(obj)
		fout.close()

		return filename

	"""
		Retrieve header and body and write file to disk.
	"""
	def __get_object_external(self, counter, url, uri) -> str:
		site, i = self.make_uri(url[2:])

		ip, soc = self.create_socket(site)
		soc.connect((ip, self.port))

		header = self.get_file("GET", url[2+i:], site, soc)

		size = self.check_page_length(header)
		filetype_1, filetype_2 = self.check_file_type(header)
		obj = self.get_object(size, soc)

		self.__close_connection(soc)

		return obj

	"""
		Uses binary format for receiving and writing objects
	"""
	def get_object(self, size:int, socket:socket) -> str:
		obj = b""

		if size == -1:
			self.get_chunked()
		else:
			while len(obj) < size:
				obj += socket.recv(size)

		return obj

	def replace_in_html(self, response, filename, url) -> str:
		return response.replace(url, filename)

	def __init__(self):
		pass