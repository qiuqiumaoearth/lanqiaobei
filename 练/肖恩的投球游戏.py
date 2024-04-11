n,q=map(int,input().split())
ls=list(map(int,input().split()))
cf_ls=[0]*(n+1)
cf_ls[0]=ls[0]
for i in range(1,n):
    cf_ls[i]=ls[i]-ls[i-1]

for j in range(q):
    l,r,c=map(int,input().split())
    cf_ls[l-1]+=c
    cf_ls[r]-=c

import itertools
qz_ls=list(itertools.accumulate(cf_ls))
for k in qz_ls[:-1]:
    print(k,end=' ')
