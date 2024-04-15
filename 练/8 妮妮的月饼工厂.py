n,k=map(int,input().split())
ls=list(map(int,input().split()))


def kf(mid):
    ans=0
    for i in ls:
        ans+=i//mid
    return ans>=k

r=10**9
l=1
jie=0
while l<=r:
    mid=(l+r)//2
    if kf(mid):
        jie = mid
        l=mid+1

    else:
        r=mid-1

#print('解',jie+1)
if jie==0:
    print(-1)
else:
    print(jie)