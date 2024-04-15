# w=int(input())
# n=int(input())
# jn=[]
# for _ in range(n):
#     jn.append(int(input()))
# jn.sort()
# #print(jn)
# zu=[]
# r=n-1
# l=0
# while l<r:
#     #print(jn[l],jn[r])
#     if jn[r]+jn[l]<=w:
#         zu.append([jn[r],jn[l]])
#         #print(zu)
#         r-=1
#         l=0
#     else:
#         r-=1
# # print(zu)
# # print(jn)
# # print(len(zu)+len(jn))

import os
import sys

# w = int(input())
# n = int(input())
# s = []
# for i in range(n):
#     s.append(int(input()))
# s.sort()
# ans = 0
# l, r = 0, n-1
# while 1:
#     if l == r:
#         ans += 1
#         break
#     # 最后两个正好配对 下标交换
#     elif l > r:
#         break
#     else:
#         if s[l] + s[r] <= w:
#             ans += 1
#             l += 1
#             r -= 1
#         else:
#
#             r -= 1
#             ans += 1
# print(ans)

w=int(input())
n=int(input())
jn=[]
for _ in range(n):
    jn.append(int(input()))
jn.sort()
l=0
r=n-1
ans=0
while True:
    if l==r:
        ans+=1
        break
    elif l>r:
        break
    else:
        if jn[l]+jn[r]<=w:
            ans+=1
            l+=1
            r-=1
        else:
            r-=1
            ans+=1
print(ans)

