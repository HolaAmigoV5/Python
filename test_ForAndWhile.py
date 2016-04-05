print('             99乘法口诀表')
list=range(1,10)
i=-1
for x in list:
	i=i+1
	j=0
	print('   ')
	while i>=j:
	    result=list[i]*list[j]
	    print('%d×%d=%d'% (list[j],list[i],result))
	    j=j+1
