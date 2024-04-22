import bisect
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

import itertools
qz_a=[0]+list(itertools.accumulate(a))
qz_b=[0]+list(itertools.accumulate(b))
# print(qz_a)
# print(qz_b)

sx=0
ans=0
for i in range(n+1):
    if qz_a[i]>k:
        break
    sx=k-qz_a[i]
    s=bisect.bisect_right(qz_b,sx)
    ans=max(ans,i+s-1)
print(ans)




























































# l=0
# r=n+m-1
#
# def shu(mid):
#     for i in range(len(qz_a)-1):
#         if qz_a[i-1]+qz_b[mid-i-1]<=k:
#             return 1
#             break
#     else:
#         return 0
#
# ans=0
# while l<r:
#     mid=(l+r)//2
#     if shu(mid):
#         ans=mid
#         l=mid+1
#     else:
#         r=mid-1
# print(ans+1)
