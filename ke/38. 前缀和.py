'''
sum[i]=sum[i-1]+a[i]
a[i]=sum[i]-sum[i-1]

即：a[l]+...+a[r]=sum[r]-sum[l-1]
'''

'''求出a的前缀和'''
# def qianzhuihe(a):
#     n=len(a)
#     sum=[0]*n
#     sum[0]=a[0]
#     for i in range(1,n):
#         sum[i]=sum[i-1]+a[i]
#     return sum
#
#
# '''求区间a[l]+....+a[r]之和'''
# def he(sum,l,r):
#     if l==0:
#         return sum[r]
#     else:
#         return sum[r]-sum[l-1]
#
# a=[1,2,3,4,5]
# sum=qianzhuihe(a)
# print('sum= ',sum)
# print(he(sum,2,4))

#二维前缀和
# ls=[[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
# ls_dui=[]
# #建立对照列表
# for _ in range(5):
#     ls_dui.append([0]*5)
# #print(ls_dui)
# for i in range(1,4):
#     for j in range(1,4):
#         if i==1:
#             ls_dui[i][j]=ls_dui
#         ls_dui[i][j]=ls[i-1][j]+ls[i][j-1]-ls[i-1][j-1]+ls[i-1][j-1]
#     print(ls_dui)



