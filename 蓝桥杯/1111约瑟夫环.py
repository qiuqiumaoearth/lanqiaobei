n,k,m=map(int,input().split())
a=list(range(1,n+1))
i=k-1
while len(a)>0:
    i=(i+m-1)%(len(a))
    print(a.pop(i))