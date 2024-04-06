t=int(input())
ls=[1]
i=1
while i < 1000001:
    a=str(i)
    sum=0
    for j in a:
        sum+=int(j)
    i+=sum
    ls.append(i)
for _ in range(t):
    n=int(input())
    if n not in ls:
        print('-1')
    else:
        print(ls.index(n))


