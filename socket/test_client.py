#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-02-17 16:44:34
# @Last Modified by:   smithallen
# @Last Modified time: 2016-02-17 17:32:03

import socket

HOST, PORT = "localhost", 8888
data = "hello server"

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket heart beat setting
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
