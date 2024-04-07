# # def qzh(a):
# #     n=len(a)
# #     sum=[0]*n
# #     sum[0]=a[0]*1
# #     for i in range(1,n):
# #         sum[i]=sum[i-1]+a[i]
# #     return sum
#
# def qv(sum,l,r):
#     if l==0:
#         return sum[r]
#     else:
#         return sum[r]-sum[l-1]
#
# n,m=map(int,input().split())
# ls=list(map(int,input().split()))
#
# 'k=1'
# sum_1=[0]*n
# sum_1[0]=ls[0]
# for i in range(1,n):
#     sum_1[i]=sum_1[i-1]+ls[i]
# #print(sum_1)
#
# 'k=2'
# sum_2=[0]*n
# sum_2[0]=ls[0]**2%(10**9+7)
# for i in range(1,n):
#     sum_2[i]=(sum_2[i-1]+ls[i]**2)%(10**9+7)
#
# 'k=3'
# sum_3=[0]*n
# sum_3[0]=ls[0]**3%(10**9+7)
# for i in range(1,n):
#     sum_3[i]=(sum_3[i-1]+ls[i]**3)%(10**9+7)
#
# 'k=4'
# sum_4=[0]*n
# sum_4[0]=ls[0]**4%(10**9+7)
# for i in range(1,n):
#     sum_4[i]=(sum_4[i-1]+ls[i]**4)%(10**9+7)
#
# 'k=5'
# sum_5=[0]*n
# sum_5[0]=ls[0]**5%(10**9+7)
# for i in range(1,n):
#     sum_5[i]=(sum_5[i-1]+ls[i]**5)%(10**9+7)
#
#
# #print(qzh(ls))
# #sum=qzh(ls)
# for _ in range(m):
#     l,r,k=map(int,input().split())
#     if k==1:
#         #print(sum_1)
#         print(qv(sum_1,l-1,r-1))
#     if k==2:
#         #print(sum_2)
#         print(qv(sum_2,l-1,r-1))
#     if k==3:
#         #print(sum_3)
#         print(qv(sum_3,l-1,r-1))
#     if k==4:
#         print(qv(sum_4,l-1,r-1))
#     if k==5:
#         print(qv(sum_5,l-1,r-1))
from itertools import accumulate
MOD = 1000000007
#求出a的前级和:
def get_presum(a):
    sum =list(accumulate(a))
    sum = [x % MOD for x in sum]
    return sum
#快速求区间a[1]+...+a[r]之和
def get_sum(sum,l,r):
    if l == 0:
        return sum[r]
    else:
        return (sum[r] - sum[l - 1] + MOD) % MOD#可能为负数
n,m=map(int,input().split())
a=list(map(int,input().split()))

#存储a数组的前缴和、a数组平方的前和、
sum_list =[]
for i in range(1,6):
    tmp_a = [x ** i for x in a]
    sum_list.append(get_presum(tmp_a))

for _ in range(m):
    l, r,k = map(int, input().split())
    print(get_sum(sum_list[k-1],l - 1, r - 1))