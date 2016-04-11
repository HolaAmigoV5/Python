#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,threading,time
#创建socket，AF_INET指定使用IPv4协议，如果使用IPv6就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定监听的IP地址和端口，此处注意是tuple
s.bind(('127.0.0.1',9999))
#开始监听，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')


def tcplink(sock,addr):
     print('Accept new connection from %s:%s...'%addr)
     sock.send(b'Welcome')
     while True:
          data=sock.recv(1024)
          time.sleep(1)
          if not data or data.decode('utf-8')=='exit':
                     break
          sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
     sock.close()
     print('Connection from %s:%s closed.'%addr)
     exit()
     
#永久循环接收客户端连接，accept()会等待并返回一个客户端的连接
while True:
    sock,addr=s.accept()     #接受一个新连接
    t=threading.Thread(target=tcplink,args=(sock,addr))   #创建新线程来处理TCP连接
    t.start()


