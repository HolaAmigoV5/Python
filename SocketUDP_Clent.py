#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#客户端
import socket
#创建socket，SOCK_DGRAM指定这个socket的类型是UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarah']:
    #发送数据
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()