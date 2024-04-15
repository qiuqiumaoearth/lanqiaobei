n,k=map(int,input().split())
ls=list(map(int,input().split()))
l=1
r=2*10**14
def pan(mid):
    res=0
    for i in ls:
        res+=min(mid,i)
    return res>=mid*k

sum=0
while l<=r:
    mid=(l+r)//2
    if pan(mid):
        sum=mid
        l=mid+1
    else:
        r=mid-1

print(sum)