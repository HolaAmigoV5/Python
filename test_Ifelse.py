# _*_ coding:utf-8 _*_
print('         小明BMI指数计算器\n*********************************************************')
name=input('请输入您的姓名：')
height=float(input('请输入您的身高(M):'))
weight=float(input('请输入您的体重(KG):'))
bmi=weight/(height*height)
print('%s的身高为%.2f，体重为%.1f,BMI指数为%.3f'% (name,height,weight,bmi))
if bmi<18.5:
     print('您的体重过轻，为：%.3f'% bmi)
elif 18.5<=bmi<25:
     print('您的体重正常，为%.3f'% bmi)
elif 25<=bmi<28:
     print('您的体重过重，为%.3f'% bmi)
elif 28<=bmi<32:
     print('您的体重肥胖，为%.3f'% bmi)
elif bmi>=32:
     print('您的体重严重肥胖，为%.3f'% bmi)
