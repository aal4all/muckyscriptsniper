#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author Falko Benthin
@Date 27.12.2015
@brief schmuddelscriptsniper checks md5-Values against database and returns ok, if it is known
"""

import socket
import threading

import md5db

class schmuddelscriptsniper(object):
	def __init__(self):
		self.BIND_IP = '0.0.0.0'
		self.BIND_PORT = 9090
		self.db = md5db.md5db()
		
	def handle_client(self,client_socket):
		request = client_socket.recv(32)
		print "[*] Received: " + request
		if self.db.getMD5(request):
			client_socket.send("true")
		else:
			client_socket.send("false")
		client_socket.close()

	def tcp_server(self):
		server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
		server.bind(( self.BIND_IP, self.BIND_PORT))
		server.listen(5)
		print"[*] Listening on %s:%d" % (self.BIND_IP, self.BIND_PORT)

		while 1:
			client, addr = server.accept()
			print "[*] Accepted connection from: %s:%d" %(addr[0], addr[1])
			client_handler = threading.Thread(target=self.handle_client, args=(client,))
			client_handler.start()

if __name__ == '__main__':
	sniper = schmuddelscriptsniper()
	sniper.tcp_server()
