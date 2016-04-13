#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#生产者-消费者模式

def consumer():      #消费者
    r=''
    while True:
        n=yield r    #通过yield拿到消息，处理，并通过yield把结果传回
        if not n:
            return
        print('[CONSUMER] Consuming %s...'% n)
        r='200 OK'
        
def produce(c):      #消费者
    c.send(None)     #启动生成器consumer对象
    n=0
    while n<5:
        n=n+1
        print('[PPRODUCE] Producing %s...'% n)
        r=c.send(n)  #切换到consumer执行，并返回r
        print('[PPRODUCE] Consumer return :%s'% r)
    c.close()
    
c=consumer()
produce(c)