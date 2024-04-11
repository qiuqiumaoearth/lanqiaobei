n=int(input())
sp=list(map(int,input().split()))
sp.sort(reverse=True)

import itertools
qzh_sp=list(itertools.accumulate(sp))

qv=[]
for i in range(n):
    if i%2!=0:
        qv.append(qzh_sp[i])
print(max(qv))
