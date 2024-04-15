import itertools
n=int(input())
ls=list(map(int,input().split()))
ls.sort(reverse=True)
sum_1=[]
for i in itertools.combinations(ls,3):
    sum_1.append(sum(i))
#print(sum_1)
a=set(sum_1)
b=list(a)
b.sort()
print(b[-3])
