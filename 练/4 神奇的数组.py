# n=int(input())
# ls=list(map(int,input().split()))
# # for i in ls:
# #     for j in ls:
# #         a=i^j
# #         print('数{},数{}，的异或值为{}'.format(i,j,a))
# #
# #前缀异或值
# qz_yh=[0]*n
# qz_yh[0]=ls[0]
# for i in range(1,n):
#     qz_yh[i]=ls[i]^qz_yh[i-1]
# print(qz_yh)
#
# import itertools
# qz_shu=list(itertools.accumulate(ls))
# print(qz_shu)
#
# l,r=0,0
# ans=0
# while l<n:
#     r=l
#     while r<n:
#         #print(r,l)
#         if qz_shu[r]-qz_shu[l]==qz_yh[r]-qz_yh[l]:
#             #print(r,l)
#
#             ans+=1
#
#         r+=1
#     l+=1
# print(ans)
#
# #方法一
# a=int(input())
# num=list(map(int,input().split()))
#
# s1=[0]*(len(num)+1)
# s2=[0]*(len(num)+1)
#
# for i in range(1,len(num)+1):
#   s1[i]=s1[i-1]+num[i-1]
#   s2[i]=s2[i-1]^num[i-1]
#
# res=0
# for i in range(len(num)):
#   # 进行二分操作
#   l,r=i,len(num)-1
#
#   ans=0
#   while l<=r:
#     mid=(l+r)//2
#
#     if s1[mid+1]-s1[i]==s2[mid+1]^s2[i]:
#
#
#       ans=mid
#       l=mid+1
#     else:
#       r=mid-1
#   res+=(ans-i+1)
#
# print(res)
#

# # 方法二
# n = int(input())
# a = list(map(int, input().split()))
# l, r, res, ans = 0, 0, 0, 0
# while l < n:
#   # 满足条件 右指针往后进行移动
#    while r < n and ((res ^ a[r]) == (res + a[r])):
#      # 移动的时候，异或上a[r]表示 考虑上 a[r]对当前 位的影响
#        res ^= a[r]
#        r += 1
#
#    ans += r - l
#    # 删除a[l]对当前位的影响
#    res ^= a[l]
#    l+=1
# print(ans)

# n=int(input())
# ls=list(map(int,input().split()))
# l,r,res,ans=0,0,0,0
# while l<n:
#     while r<n and (res^ls[r])==(res+ls[r]):
#         res^=ls[r]
#         r+=1
#     ans+=r-l
#     res^=ls[l]
#     # l+=1
# print(ans)

n=int(input())
ls=list(map(int,input().split()))
l,r,res,ans=0,0,0,0
while l<n:
    while r<n and (res^ls[r])==(res+ls[r]):
        res^=ls[r]
        r+=1
    ans += r - l
    res^=ls[l]
    l+=1
print(ans)








