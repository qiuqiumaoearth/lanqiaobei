n,w=map(int,input().split())
cf_ls=[0]*(2*100000+10)
for _ in range(n):
    s,t,p=map(int,input().split())
    cf_ls[s]+=p
    cf_ls[t]-=p

import itertools
qz_ls=list(itertools.accumulate(cf_ls))
if max(qz_ls)>w:
    print('No')
else:
    print('Yes')