n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
zong=[]
for i in range(n):
    zong.append([a[i],b[i],a[i]+b[i]])
zong=sorted(zong,key=lambda x:x[2])

qz_zong=[]
for i in zong:
    qz_zong.append(i[2])

import itertools
qz_zong=list(itertools.accumulate(qz_zong))

import bisect
wz=bisect.bisect_left(qz_zong,k)

zh=sorted(zong[wz:],key=lambda x:x[0])
#print(zh)

if zh[0][0]+qz_zong[wz-1]<=k:
    print(wz+1)
else:
    print(wz)



