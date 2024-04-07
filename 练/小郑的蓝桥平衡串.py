# n=input()
# l=len(n)
# ls_n=[]
# for i in n:
#     if i=='L':
#         ls_n.append(-1)
#     else:
#         ls_n.append(1)
#
#
# #前缀和
# ls_zhui=[0]*l
# ls_zhui[0]=ls_n[0]
# for i in range(1,l):
#     ls_zhui[i]=ls_zhui[i-1]+ls_n[i]
#
# # print(ls_n)
# print(ls_zhui)
#
# ans=0
# #xunzhao   10的三次方
# for i in range(0,l):
#     for j in range(i,l):
#         #print(i,j)
#         #print(ls_zhui[i], ls_zhui[j])
#         if ls_zhui[i]-ls_zhui[j]==0:
#             print(ls_zhui[j],ls_zhui[i])
#             ans=max(ans,j-i+1)
# print(ans)



# s = list(input().strip())
# n = len(s)
#
# # 映射
# for i in range(n):
#     if s[i] == 'Q':
#         s[i] = 1
#     else:
#         s[i] = -1
#
# # 前缀和
# pre_sum = [0] * (n+1 )
# pre_sum[0] = s[0]
# for i in range(1, n):
#     pre_sum[i] = pre_sum[i - 1] + s[i]
#
# print(pre_sum)
# # 枚举子区间，子区间和为0：数量相等，找最长子区间
# ans = 0
# for l in range(0, n):
#     for r in range(l, n):
#         print(pre_sum[r],pre_sum[l-1])
#         if pre_sum[r] - pre_sum[l - 1] == 0:
#             ans = max(ans, r - l + 1)
#
# print(ans)



# ls=[1,2,3,4]
# for i in range(4):
#     for j in range(i,4):
#         print(i,j)


str=input()
n=len(str)
ls_pre=[]
for i in str:
    if i=='L':
        ls_pre.append(-1)
    else:
        ls_pre.append(1)
#print(ls_pre)
#前缀和
ls_sum=[0]*n
ls_sum[0]=ls_pre[0]
for i in range(1,n):
    ls_sum[i]=ls_sum[i-1]+ls_pre[i]
#print(ls_sum)
ans=0
for l in range(0,n):
    for r in range(l+1,n):
        if abs(ls_sum[l]-ls_sum[r])==1 :
            if str[l:r+1].count('Q')==(r-l+1)//2:
                ans=max(ans,r-l+1)
                #print(r-l+1)
print(ans)



