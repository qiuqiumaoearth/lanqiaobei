n,k=map(int,input().split())
jg=list(map(int,input().split()))
jg.sort()

import itertools
import math
qz_jg=list(itertools.accumulate(jg))
#print(qz_jg)

ge=0
qian=0
f=0
for i in range(n):
    if qz_jg[i]>k:
        f=1
        qian=qz_jg[i]
        ge=i
        break

a=math.ceil(jg[i]/2)
if f==1:
    if qian-jg[i]+a<=k:
        print(ge+1)
    else:
        print(ge)
else:
    print(n)




# import math
# a=5/2
# print(math.floor(a))
#
