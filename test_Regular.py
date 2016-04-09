#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
#∆•≈‰some@gmail.com
#print(re.match(r'(\w+.)?\w+@\w+.(com|cn|org)','bill.gates@microsoft.cn'))
print(re.match(r'(<[a-zA-Z]+\s*[a-zA-Z]+>)\s?\w+@\w+\.(com|cn|org)','<Tom Paris> tom@voyager.org').group(1))