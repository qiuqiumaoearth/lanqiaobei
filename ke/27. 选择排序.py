n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    min_value=a[i]
    min_idx=i
    for j in range(i,n):
        if a[j]<min_value:
            min_value=a[j]
            min_idx=j
    a[min_idx],a[i]=a[i],a[min_idx]
    print(a)
