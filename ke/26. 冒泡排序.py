a=[9,3,1,6,7]
temp=0
b=a
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

    print(a)

