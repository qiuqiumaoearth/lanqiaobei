n=int(input())
ls=list(map(int,input().split()))
ls.sort()
ss=[]
for i in range(1,n):
    ss.append(ls[i]-ls[i-1])
print(min(ss))
