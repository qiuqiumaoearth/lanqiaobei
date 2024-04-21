n,k=map(int,input().split())
qkl=[]
for _ in range(n):
    h,w=map(int,input().split())
    qkl.append([h,w])

l=0
r=1000000
mid=(l+r)//2
ls=[l,r]
while ls[-1]!=ls[-2]:
    mid=(l+r)//2
    sum=0
    ls.append(mid)
    for i in qkl:
        a=(i[0]//mid)*(i[1]//mid)
        sum+=a
    if sum<k:
        r=mid
    else:
        l=mid
print(ls[-1])



