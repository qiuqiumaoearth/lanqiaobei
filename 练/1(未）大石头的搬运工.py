n=int(input())
ls=[]
for _ in range(n):
    a,b=map(int,input().split())
    ls.append([b,a])

ls.sort(key=lambda x:x[0])
print(ls)

shu_q=[]
shu_h=[]
shu=[]
#对于每个点进行计算
shu_q.append(0)
for i in range(1,n):
    shu_q.append((ls[i][0]-ls[i-1][0]))*ls[i][1]

# for j in range(0,n-1):