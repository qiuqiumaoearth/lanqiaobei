t=int(input())
for _ in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    dong=0
    ans=0
    for i in ls:
        ans+=i
        if i==0 :
            ans+=1
            dong+=1
    if ans==0:
        dong+=1
    print(dong)


