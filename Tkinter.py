#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()        #��Widge���뵽��������
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel=Label(self,text='Hello world!')   #����һ��Label
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)   #����һ��Button
        self.quitButton.pack()
app=Application()
#���ô��ڱ���
app.master.title('Hello World')
#����Ϣѭ��
app.mainloop()