# n,m,b=map(int,input().split())
# gy={}
# for i in range(n):
#     a,c=map(int,input().split())
#     if c not in gy:
#         gy[c]=a
#     else:
#         if a>gy[c]:
#             gy[c]=a
#
# a=sorted(gy.items(),key=lambda x:x[0],reverse=True)
# print(a)
#
# dr_m=0
# for j in range(m):
#     dr=int(input())
#     if dr>dr_m:
#         dr_m=dr
#
#
# import itertools
# qzz_fy=[]
# for ff in a:
#     #print(ff)
#     qzz_fy.append(ff[0])
# qz_fy=list(itertools.accumulate(qzz_fy))
#
# qzz_sh=[]
# for ss in a:
#     qzz_sh.append(ss[1])
# qz_sh=list(itertools.accumulate(qzz_sh))
#
#
# qz_sh.append(0)
# qz_fy.append(0)
#
# print("伤害前缀和",qz_sh)
# print("费用前缀和",qz_fy)
#
# zong=[]
# l=-1
# r=0
# f=0
# while r<=len(qz_sh)-1:
#
#     if qz_fy[r]-qz_fy[l]<=b:
#         dd=qz_sh[r]-qz_sh[l]
#         if dd>=dr_m:
#             f=1
#         zong.append(dd)
#         r+=1
#     else:
#         l+=1
#
#     if f==1:
#         break
# print(zong)


n,m,B=map(int,input().split())#
gan=[[0,0]]
di=[]
for i in range(n):
  gan.append(list(map(int,input().split())))
gan.sort(key=lambda x:(x[1],-x[0]))#优先攻击高的，费用低的。
for i in range(m):
  di.append(int(input()))
di.sort(reverse=True)
#背包不就对了？攻击力=价值。
# dp=[[0]*(B+1) for i in range(n+1)]
# #在B预算下，找到攻击最高的干员组，并计算他们每轮总攻击，
# #对最大的敌人需要几回合击败，则是最小回合数。

# for i in range(1,n+1):#对于前n个干员。
#   for j in range(1,B+1):#逐渐增大的预算。
#     if gan[i][1]<=j:#当前干员比当前预算低，
#       dp[i][j]=max(dp[i-1][j],dp[i-1][j-gan[i][1]]+gan[i][0] )
#     else:
#       dp[i][j]=dp[i-1][j]#此体积下，有你没你一样。
# total=dp[n][B]
# if total==0:
#   print(-1)
# elif di[0]%total==0:
#   print(di[0]//total)
# else:
#   print(di[0]//total+1)
# 二维超一点点内存，则一维优化！
dp=[0]*(B+1)
for i in range(1,n+1):
  for j in range(B,1,-1):
    if gan[i][1]<=j:
      dp[j]=max(dp[j],dp[j-gan[i][1]]+gan[i][0])
total=dp[B]
if total==0:
  print(-1)
elif di[0]%total==0:
  print(di[0]//total)
else:
  print(di[0]//total+1)