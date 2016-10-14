#!/usr/bin/env python

import socket as skt 
import sys
from urlparse import urlparse


#make http request
def make_http_request(host, obj):
    NL="\r\n"
    return ("GET {o} HTTP/1.1" + NL + "Host: {s}" + NL + NL).format(o=obj, s=host)


#extract header from the first .recv
def header_cutter(s):
	f=s.split("\r\n\r\n")
	return f[0]


#extract content length from header
def content_length(s):
	f=s.split("\r\n")
	for e in f:
		if "Content-Length" in e:
			return e.split(":")


#get header 
def get_header(client_socket):
	header=""
	while True:
		data_received = client_socket.recv(8192)
		header+=data_received
		if "\r\n\r\n" in data_received:
			break
			
	return header


#load and write data
def load_write_data(byte_count, contentlength, client_socket, f):
	while byte_count<=contentlength:
		data_received = client_socket.recv(8192)
		f.write(data_received)
		if len(data_received)+byte_count==contentlength:
			byte_count+=len(data_received)
			client_socket.close()
			break
		byte_count+=len(data_received)
	return byte_count


def main():
	url = sys.argv[-1]
	urlp= urlparse(url)

    #srv name and path
	srv_name = urlp.hostname
	srv_path = urlp.path
	if ":" in url:
		srv_port = urlp.port 
	else:
		srv_port = 80
	
	#create socket and connection
	client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
	client_socket.connect((srv_name, srv_port))

	#make and send
	request_str = make_http_request(srv_name, srv_path)
	client_socket.send(request_str)
	
	#write and load file from http
	with open(sys.argv[2], 'wb') as f:
		byte_count=0
		## TO FIX: use argparse or getopt
		if sys.argv[1] == "-o":
			#get header
			header= get_header(client_socket)
			h = header_cutter(header)
			content = header.split("\r\n\r\n")[1]

			#for chunk
			if ("Transfer-Encoding: chunked" in h) or ("chunked" in h) or ("Chunked" in h):
				print "I die here"

			#if content length exsist in header
			elif "Content-Length" in h:
				contentlength = int(content_length(h)[1])
				byte_count+=len(content)
				#write the remaining content
				f.write(content)

				#load and write data
				byte_count=load_write_data(byte_count, contentlength, client_socket, f)


if __name__ == '__main__':
	main()
