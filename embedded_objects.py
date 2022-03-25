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

	def __get_header(self, command, url, uri, soc):
		request = command + " /" + url + " HTTP/1.1\r\nHost: " + uri + "\r\n\r\n"
		soc.send(request.encode())

		buffer = ""
		while self.end_of_header not in buffer:
			buffer += soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

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

	def retrieve_embedded_objects(self, response, soc, uri):
		self.file_extensions = [self.file_extensions[1]]
		counter = 0
		url = ""

		for extension in self.file_extensions:
			index = 0

			while response.find(extension) != -1:
				index = response.find(extension) + len(extension) - 1

				while response[index] not in self.end_chars:
					url = response[index] + url
					index -= 1

				start = index

				header = self.__get_header("GET", url, uri, soc)
				size = self.check_page_length(header)
				filetype_1, filetype_2 = self.check_file_type(header)
				object = self.get_object(size, soc)		

				filename = uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
				fout = open(filename, "wb")
				fout.write(object)
				fout.close()

				self.replace_in_html(filename, index)

				response = response[(index + len(filename)):]

				counter += 1	

	"""def retrieve_embedded_objects(self, response):
		counter = 0
		image = b""
		working_response = response

		for s in self.file_extensions:
			index = 0

			while working_response.find(s) != -1:
				org_index = working_response[index:].find(s) + len(s) - 1
				index = org_index

				if not ((ord(response[index+1]) >= 65 and  ord(response[index+1]) <= 90) or (ord(response[index+1]) >= 97 and  ord(response[index+1]) <= 122)):
					url = ""

					while response[index] not in self.end_chars:
						url = response[index] + url
						index -= 1

					header = ""
					if url[:2] == "//":
						site, i = self.make_uri(url[2:])

						ip, soc = client.self.create_socket(site)
						soc.connect((ip, self.port))

						header = client.self.get_object("GET", url[2+i:], site, soc)

						size = client.self.check_page_length(header)
						filetype_1, filetype_2 = client.self.check_file_type(header)
						image = self.get_object(size, soc)
					elif url[:8] == "https://":
						site, i = self.make_uri(url[8:])

						ip, soc = client.self.create_socket(site)
						soc.connect((ip, self.port))

						header = self.get_object("GET", url[2+i:], site, soc)

						size = self.check_page_length(header)
						filetype_1, filetype_2 = self.check_file_type(header)
						image = self.get_object(size, soc)
					else:
						header = self.get_object("GET", url, self.uri, self.soc)

						size = self.check_page_length(header)
						filetype_1, filetype_2 = self.check_file_type(header)
						image = self.get_object(size, self.soc)

					if url[:2] == "//":
						client.close_connection(soc)
					if url[:8] == "http://":
						client.close_connection(soc)

					filename = self.uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
					fout = open(filename, "wb")
					fout.write(image)
					fout.close()

					working_response, start = self.replace_in_html(filename, org_index)

					index = start + len(filename)
					working_response = working_response[index:]

					counter += 1"""

	"""
		Uses binary format for receiving and writing objects
	"""
	def get_object(self, size, socket):
		obj = b""

		if size == -1:
			self.get_chunked()
		else:
			while len(obj) < size:
				obj += socket.recv(size)

		return obj

	"""
		
	"""
	def replace_in_html(self, filename, index):
		# def start_org_filepath():
		# 	i = 0

		# 	while self.response[index-i] not in self.end_chars:
		# 		i += 1
				
		# 	return index - i

		start = index #start_org_filepath()
		# filename_x = ""
		# for i in filename:
		# 	filename_x += "x"

		sta_string = response[:start + 1]
		end_string = response[index + len(filename) + 1:]

		response = sta_string + filename + end_string
		# working_response = sta_string + filename_x + end_string

		return response

	def __init__(self):
		pass