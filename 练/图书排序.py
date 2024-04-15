a=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    a.append([x,y])
a.sort(key=lambda x:x[1])
for j in range(len(a)):
    print(a[j][0])