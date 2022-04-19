import sys, socket
from typing import Tuple, Union

class Util:
	BUFFERSIZE = 1

	end_of_header = "\r\n\r\n"
	stop = "\r\n"

	file_extensions = [".jpg", ".webp", ".png", ".js", ".css", ".gif", ".PNG", ".JPG"]
	end_chars = ["\"", "\'", "(", "=", ")"]
	
	charset = "utf-8"
	filetype = ""

	def create_socket(self, uri:str) -> Tuple[str, socket.SocketKind]:
		if uri[:3] == "www":
			ip = socket.gethostbyname(uri)
		elif uri == "localhost":
			ip = "127.0.0.1"
		else:
			ip = uri
		
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(5)
		except socket.error as e:
				print(e)

		return ip, soc

	def connect_socket(self, soc:socket.SocketKind, ip:str, port:str):
		try:
			soc.connect((ip, port))
		except socket.error as e:
			print(e)

	def close_connection(self, soc:socket.SocketKind):
		soc.shutdown(socket.SHUT_RDWR)
		soc.close()

	"""
		Checks the charset in the header and sets the correct global charset.
		Standard charset is utf-8.
	"""
	def check_charset(self, header:str):
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
	def get_header(self, soc:socket.SocketKind) -> str:
		buffer = ""
		
		while self.end_of_header not in buffer:
			buffer += soc.recv(self.BUFFERSIZE).decode(encoding=self.charset)

		return buffer

	def write_output(self, uri:str, filetype_1:str, filetype_2:str, obj:Union[bytes, str], counter:str="") -> str:
		if filetype_2 == "plain":
			self.filetype = "txt"
		else:
			self.filetype = filetype_2

		filename = ""

		if counter == "":
			print(uri + "." + self.filetype)	#	debug
			fout = open(uri + "." + self.filetype, mode="wb")
			fout.write(obj.encode(encoding=self.charset))
		else:
			filename = uri + "_" + filetype_1 + "_" + str(counter) + "." + filetype_2
			fout = open(filename, mode="wb")
			fout.write(obj)

		fout.close()

		return filename

	def replace_in_html(self, response:str, filename:str, url:str) -> str:
		return response.replace(url, filename)

	def __init__(self):
		pass