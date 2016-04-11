#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

#格式化邮件地址
def _format_addr(s):
    name,addr=parseaddr(s)
    #不能简单传入name<addr@example.com>,因为如果包含中文，需要通过Header对象进行编码
    return formataddr((Header(name,'utf-8').encode(),addr))
    
#输入Email地址和口令
from_addr=input('From:')
password=input('Password:')
#输入收件人的地址：
to_addr=input('To:')
#输入SMTP服务器的地址：
smtp_server=input('SMTP Server:')
#输入传输端口
smtp_port=input('SMTP Port:')

#构造MIMEText对象，第一个参数邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
#最终的MIME就是'text/plain'，最后一个参数用utf-8编码保证多语言兼容性
#带附件的邮件，可以构造一个MIMEMultipart对象，然后加一个MIMEText作为邮件正文，再继续加MIMEBase对象即可
#msg=MIMEText('hello,send by Python...','plain','utf-8')

#msg=MIMEMultipart()

#同时支持HTML和Plain格式，如果收件人无法查看HTML格式的邮件，自动降级查看纯文本邮件
msg=MIMEMultipart('alternative')  #利用MIMEMultipart组合一个HTML和Plain，要注意指定subtype是alternative

#发送html邮件时，需要把第二个参数修改为html
#msg=MIMEText(''<html><body><h1>Hello</h1>' +'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>','html','utf-8')
    
msg['From']=_format_addr('地球人<%s>'%from_addr)
msg['To']=_format_addr('Aministrator<%s>' %to_addr)
msg['Subject']=Header('来自火星的邮件...','utf-8').encode()

#邮件正文是MIMEText:
msg.attach(MIMEText('hello,send by Python...','plain','utf-8'))

#邮件正文中嵌入图片，在html中通过引用src='cid:0'就可以把附件昨晚图片嵌入了。如果有多个图片，就依次编号，然后引用不同的cid:x即可
msg.attach(MIMEText('<html><body><h1>Hello,我是外星人，我马上要统治地球了。哈哈哈哈哈哈！！！</h1>' +
    '<p><img src="cid:0"></p>' +
    '<p><img src="cid:1"></p>' +
    '</body></html>', 'html', 'utf-8'))


#添加附件就是添加一个MIMEBase对象，从本地读取一个图片
with open('C:/Users/Administrator/Desktop/Python/11.jpg','rb') as f:
    #设置附件的MIME和文件名
    mime=MIMEBase('image','jpg',filename='11.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='11.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart:
    msg.attach(mime)
    
#添加第二张附件就是添加一个MIMEBase对象，从本地读取一个图片
with open('C:/Users/Administrator/Desktop/Python/22.png','rb') as f:
    #设置附件的MIME和文件名
    mime=MIMEBase('image','png',filename='22.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='11.jpg')
    mime.add_header('Content-ID','<1>')
    mime.add_header('X-Attachment-Id','1')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart:
    msg.attach(mime)

#server=smtplib.SMTP(smtp_server,25)  #SMTP协议默认端口25，不加密传输
server=smtplib.SMTP(smtp_server,smtp_port)  #SMTP协议默认端口25，这里取输入的端口
#server.starttis()                    #调用starttis()建立SSL安全连接
#server.set_debuglevel(1)             #打印出与SMTP服务器交互的所有信息
# ehlo命令，docmd方法包括了获取对方服务器返回信息，如果支持安全邮件，返回值里会有starttls提示 
server.docmd( " EHLO server " )
server.login(from_addr,password)     #登录SMTP服务器
#发送邮件，由于可以发送给多个人，所有传入一个list，邮件正文是str，as_string()把MIMETest对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

