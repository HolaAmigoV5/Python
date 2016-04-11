#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket,threading,time
#����socket��AF_INETָ��ʹ��IPv4Э�飬���ʹ��IPv6��ָ��ΪAF_INET6��SOCK_STREAMָ��ʹ����������TCPЭ��
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#�󶨼�����IP��ַ�Ͷ˿ڣ��˴�ע����tuple
s.bind(('127.0.0.1',9999))
#��ʼ����������Ĳ���ָ���ȴ����ӵ��������
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
     
#����ѭ�����տͻ������ӣ�accept()��ȴ�������һ���ͻ��˵�����
while True:
    sock,addr=s.accept()     #����һ��������
    t=threading.Thread(target=tcplink,args=(sock,addr))   #�������߳�������TCP����
    t.start()


