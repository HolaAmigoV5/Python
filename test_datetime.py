#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
      h=re.match(r'UTC([\+|\-]\d{1,2}):(\d+)',tz_str).groups()  #时区信息匹配
      hh=0
      print(h[0],'******',h[1])
      #时区信息转换
      if int(h[1])==0:
         hh=int(h[0])
      else:
         hh=int(h[0])+(int(h[1])/60)
      print(hh)
      tz_utc=timezone(timedelta(hours=hh))  #创建指定时区
      utc_dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc)  #str转换为datetime，并转换我指定时区的UTC时间
      print(utc_dt.timestamp())   #转换并打印出timestamp时间
      return utc_dt.timestamp()
     

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

t3 = to_timestamp('2015-5-31 16:10:30', 'UTC+06:30')
assert t3 == 1433065230.0, t3

print('Pass')