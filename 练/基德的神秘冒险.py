# import itertools
# ls=[2,4,2,1,4]
# for i in itertools.combinations(ls,3):
#     print(min(i))

import itertools
n,q=map(int,input().split())
ls=list(map(int,input().split()))
ls.sort()
gs=[]
for i in range(n):
    a=(n-i-1)*(n-i-2)//2
    gs.append(a)
#print(gs)

#前缀和
gs=list(itertools.accumulate(gs))
#print(gs)

import bisect
for j in range(q):
    b=int(input())
    c=bisect.bisect_left(gs,b)
    print(ls[c])




