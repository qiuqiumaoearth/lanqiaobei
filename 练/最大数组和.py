# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     ls=list(map(int,input().split()))
#     sum_1=sum(ls)
#     ls.sort()
#     for i in range(k):
#         xiao=ls[0]+ls[1]
#         da=ls[-1]
#         if xiao>=da:
#             sum_1-=da
#             ls.pop(-1)
#         else:
#             sum_1-=xiao
#             ls.pop(1)
#             ls.pop(0)
#     print(ls)

# import itertools
# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     baoshi=list(map(int,input().split()))
#     baoshi.sort()
#
#     #前缀和
#     ls=list(itertools.accumulate(baoshi))
#     #print(ls)
#     ls.append(0)
#
#     jiazhi=[]
#     jiazhi.append(ls[n-k-1])
#     jiazhi.append(ls[n-1]-ls[k*2-1])
#     pos=0
#     print(jiazhi)
#     #for i in range(k-1):

# from itertools import accumulate
# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     jz=list(map(int,input().split()))
#     jz.sort()
#     sum_jz=sum(jz)
#
#     qz_jz=list(accumulate(jz))
#     #print(qz_jz)
#     # sum_jz=sum(jz)
#     kn = []
#     kn.append(qz_jz[2*k-1])
#     kn.append(qz_jz[-1]-qz_jz[-(k+1)])
#     # for i in range(k):
#     # print(kn)
#     for i in range(1,k):
#         #print(qz_jz[2*(i)-1],qz_jz[-1],qz_jz[-k-i+1])
#         a=qz_jz[2*(i)-1]+qz_jz[-1]-qz_jz[-k-i+1]
#         kn.append(a)
#     #print(kn)
#     print(sum_jz-min(kn))
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    aa = [0]
    ans = -1
    for i in range(1, n + 1):  # aa[0]=0  从aa[1]开始，代表a数组的前缀和 aa[1]代表 a[0] aa[2] 代表a[0]+a[1]
        aa.append(aa[i - 1] + a[i - 1])  # 构造前缀和
    for i in range(k + 1):
        maxans = aa[n - (k - i)] - aa[2 * i]  # i代表操作次数，2*i就是删掉两个最小值的操作次数 k-i就是删掉最大值的操作次数
        # 每进行一次删除两个最小值，前缀和就要去掉一个左端点，每删除一个最大值，前缀和就要去掉一个右端点
        # 枚举 全部进行最小值删除 全部进行最大值删除 和混合删除的剩下的最大值
        ans = max(ans, maxans)

    print(ans)
