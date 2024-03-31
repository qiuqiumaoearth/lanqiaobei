a=int(input())
n=list(map(int,input().split()))
dict={}
ans=0
for i in n:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for j in dict:
    if j<=dict[j]:
        ans+=1

print(ans)