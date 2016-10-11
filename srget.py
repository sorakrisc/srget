#!usr/bin/env python

import socket as skt 
import sys
from urlparse import urlparse

def make_http_request(host, obj):
    NL="\r\n"
    return ("GET {o} HTTP/1.1" + NL + "Host: {s}" + NL + NL).format(o=obj, s=host)
def header_cutter(s):
	f=s.split("\r\n\r\n")
	return f[0]
def contentlength(s):
	f=s.split("\r\n")
	for e in f:
		if "Content-Length" in e:
			return e.split(":")
url = sys.argv[-1]
urlp= urlparse(url)
srv_name = urlp.netloc
srv_path = urlp.path
srv_port = 80
print srv_port
print srv_name
srv_ip = skt.gethostbyname(srv_name) #"21.224.123.42:231"
print srv_ip

client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client_socket.connect((srv_name, srv_port))
print "connencting"

request_str = make_http_request(srv_name, srv_path)
client_socket.send(request_str)
print "request sent"

f = open(sys.argv[2], 'wb')
header=""
byteCount=0
if sys.argv[1] == "-o":
	print "pass"
	#find\r\n\r\n
	while True:
		data_received = client_socket.recv(8192)
		header+=data_received
		if "\r\n\r\n" in data_received:
			break
			client_socket.close()
	h = header_cutter(header)
	contentlength = int(contentlength(header)[1])
	content = header.split("\r\n\r\n")[1]
	byteCount+=len(content)
	f.write(content)
	print contentlength
	print "SECOND"

	while byteCount<=contentlength:
		data_received = client_socket.recv(8192)
		print "hello world!"
		f.write(data_received)
		if len(data_received)+byteCount==contentlength:
			byteCount+=len(data_received)
			print len(data_received)+byteCount
			client_socket.close()
			break
		byteCount+=len(data_received)
		print byteCount
		# print "yo"
		# print "{!r}".format(data_received), #, prevent from making a new line
	

print byteCount==contentlength
print byteCount
print contentlength
print "DONE"


#if connection break 
#if there is no more data
#did ech round data is sent 1024
#input thong mee http paow ans mee
#load 32 bit

