'''比大小'''
# def MAX(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# a,b=map(int,input().split())
# print(MAX(a,b))

'''阶乘函数'''
# def factorial(x):
#     a=1
#     for i in range(1,x+1):
#         a=a*i
#     return a
#
# sum=0
# for j in range(1,11):
#     sum+=factorial(j)
# print(sum)

#列表字典传递是可变的

#不定长参数
'''功能:计算传递所有参数的绝对值之和'''
'''将它组装成一个元组'''
# def grt_abs_sum(*num):
#     ans=0
#     for x in num:
#         ans+=abs(x)
#     return ans
#
# print(grt_abs_sum(1,-2,-9,10))


''''组装成字典'''
# def f(a,b,**ll):
#     print('a= ',a)
#     print('b= ',b)
#     print("ll= ",ll)
#
# f(1,2,c=1,d=4,e=10)

'''在函数内部使用全局变量
        global'''

