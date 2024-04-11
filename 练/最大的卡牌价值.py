# n,k=map(int,input().split())
# ls_a=list(map(int,input().split()))
# ls_b=list(map(int,input().split()))
#
# jz=sum(ls_a)
# kebian=[]
# for i in range(n):
#     if ls_b[i]>ls_a[i]:
#         kebian.append([ls_b[i],ls_a[i]])
#
# kebian.sort(key=lambda x:x[0],reverse=True)
# #print(kebian)
# # for j in range(k):
# #     a=kebian[j]
# #     jz-=a[1]
# #     jz+=a[0]
# # print(jz)
# while len(kebian)!=0 and k!=0:
#     a=kebian.pop(0)
#     jz-=a[1]
#     jz+=a[0]
#     k-=1
# print(jz)

# n,k=map(int,input().split())
# ls_a=list(map(int,input().split()))
# ls_b=list(map(int,input().split()))
# chazhi=[]
# for i in range(n):
#     chazhi.append([i,ls_a[i]-ls_b[i]])
# #print(chazhi)
# chazhi.sort(key=lambda x:x[1],reverse=True)
# #print(chazhi)
# jz=sum(ls_a)
# for _ in range(k)

# n,k=map(int,input().split())
# ls_a=list(map(int,input().split()))
# ls_b=list(map(int,input().split()))
# chazhi=[]
# for i in range(n):
#     chazhi.append([i,ls_a[i]-ls_b[i]])
# #print(chazhi)
# chazhi.sort(key=lambda x:x[1],reverse=True)
# #print(chazhi)
# jz=sum(ls_a)
# for j in range(k):
#     if chazhi[j][1]>0:
#         jz+=chazhi[j][1]
# print(jz)

# import os
# import sys
#
# # 请在此输入您的代码
# n, k = map(int, input().split())
# zheng = list(map(int, input().split()))
# fan = list(map(int, input().split()))
# c = []
# ss = sum(zheng)
# for i in range(n):
#     if fan[i] - zheng[i] >= 0:
#         c.append(fan[i] - zheng[i])
#
# c.sort(reverse=True)
# a = ss + sum(c[:k])
# print(a)


n,k=map(int,input().split())
ls_a=list(map(int,input().split()))
ls_b=list(map(int,input().split()))
chazhi=[]
for i in range(n):
    if ls_a[i]<ls_b[i]:
        chazhi.append(ls_b[i]-ls_a[i])
#print(chazhi)

jz=sum(ls_a)
chazhi.sort(reverse=True)
if len(chazhi)<k:
    jz+=sum(chazhi)
else:
    jz+=sum(chazhi[:k])
print(jz)


