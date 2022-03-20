import client, sys

client.ClientSocket("GET", sys.argv[2], "80")
client.ClientSocket("GET", "www.example.com", "80")
client.ClientSocket("GET", "www.tcpipguide.com", "80")
client.ClientSocket("GET", "www.jmarshall.com", "80")
client.ClientSocket("GET", "www.tldp.org", "80")
client.ClientSocket("GET", "www.tinyos.net", "80")
client.ClientSocket("GET", "www.linux-ip.net", "80")
