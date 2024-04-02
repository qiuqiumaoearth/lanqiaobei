n=int(input())
ls=list(map(int,input().split()))
ls.sort()
mm=[]
for i in range(1,n):
    mm.append(ls[i]-ls[i-1])
print(min(mm))