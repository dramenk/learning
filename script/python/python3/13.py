#!/usr/bin/python3

import socket

# IPV4, for TCP
st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish a connection
st.connect(('baidu.com', 80))
st.close()

# IPV4, for UDP
su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
su.close()


