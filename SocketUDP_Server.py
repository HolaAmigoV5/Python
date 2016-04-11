#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#服务器端
import socket
#创建socket，SOCK_DGRAM指定这个socket的类型是UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999....')
while True:
    #接收数据
    data,addr=s.recvfrom(1024)             #fecvfrom()返回数据和客户端的地址和端口
    print('Received from %s:%s.'%addr)
    s.sendto(b'Hello,%s!'%data,addr)       #sendto()将数据发送给指定的地址和端口客户端