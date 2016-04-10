#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()        #把Widge加入到父容器中
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel=Label(self,text='Hello world!')   #创建一个Label
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)   #创建一个Button
        self.quitButton.pack()
app=Application()
#设置窗口标题
app.master.title('Hello World')
#主消息循环
app.mainloop()