#暴力
# t=int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     ls=list(map(int,input().split()))
#
#     cnt=[]
#     for i in range(1,61):
#         num=0
#         j=0
#         while j<n:
#             if ls[j]!=i:
#                 num+=1
#                 j+=k
#                 continue
#             j+=1
#         cnt.append(num)
#     print(cnt)

import os
import sys

# 请在此输入您的代码
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    cnt=[]
    for i in range(1,61):
        num=0
        j=0
        while j<n:
            if a[j]!=i:
                num+=1
                j+=k
                continue

            j+=1

        cnt.append(num)
    print(min(cnt))



# for i in range(0,n,k):
#     print(ls[i:i+2])