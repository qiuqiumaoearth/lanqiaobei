n=int(input())
ls=list(map(int,input().split()))
#print(ls)
ls.sort()
for i in ls:
    print(i,end=' ')