# n=int(input())
# ls=[]
# for _ in range(n):
#     a,b=map(int,input().split())
#     ls.append([b,a])
#
# ls.sort(key=lambda x:x[0])
# print(ls)
#
# shu_q=[]
# shu_h=[]
# shu=[]
# #对于每个点进行计算
# shu_q.append(0)
# for i in range(1,n):
#     shu_q.append((ls[i][0]-ls[i-1][0]))*ls[i][1]
#
# # for j in range(0,n-1):

n=int(input())
shitou=[]
for _ in range(n):
    w,p=map(int,input().split())
    shitou.append([p,w])
shitou.sort(key=lambda x:x[0])
#print(shitou)

#前缀和
ls_qian=[0]*n
ls_qian[0]=shitou[0][1]
for i in range(1,n):
    ls_qian[i]=ls_qian[i-1]+shitou[i][1]
#print(ls_qian)

per_sum=[0]
for i in range(1,n):
    per_sum.append((shitou[i][0]-shitou[i-1][0])*ls_qian[i-1]+per_sum[i-1])
#print(per_sum)

#后缀和
shitou.sort(key=lambda x:x[0],reverse=True)
#print(shitou)

ls_hou=[0]*n
ls_hou[0]=shitou[0][1]
for i in range(1,n):
    ls_hou[i]=ls_hou[i-1]+shitou[i][1]
#print(ls_hou)

ls_sum=[0]
for i in range(1,n):
    ls_sum.append((shitou[i-1][0]-shitou[i][0])*ls_hou[i-1]+ls_sum[i-1])
#print(ls_sum)
ls_sum.reverse()

ls=[]
for i in range(n):
    ls.append(ls_sum[i]+per_sum[i])
print(min(ls))