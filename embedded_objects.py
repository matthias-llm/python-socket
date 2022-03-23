class Embedded_Objects:
	file_extensions = [".jpg", ".png", ".js", ".css", ".gif"]
	end_chars = ["\"", "\'", "(", "="]
	response = ""

	def make_uri(self, url):
		u = ""
		index = 0

		while url[index] != "/":
			u += url[index]
			index += 1
		
		return u, index

	def retrieve_embedded_objects(self, response):
		pass

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

	def __init__(self, response):
		self.retrieve_embedded_objects(response)