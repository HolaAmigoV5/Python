#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#��������
import socket
#����socket��SOCK_DGRAMָ�����socket��������UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#�󶨶˿�
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999....')
while True:
    #��������
    data,addr=s.recvfrom(1024)             #fecvfrom()�������ݺͿͻ��˵ĵ�ַ�Ͷ˿�
    print('Received from %s:%s.'%addr)
    s.sendto(b'Hello,%s!'%data,addr)       #sendto()�����ݷ��͸�ָ���ĵ�ַ�Ͷ˿ڿͻ���