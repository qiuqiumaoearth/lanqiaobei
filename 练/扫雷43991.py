n,m=map(int,input().split())
ls=[]
pp=[]
ls.append([0]*(m+2))
pp.append([0]*(m+2))
for _ in range(n):
    a=[0]+list(map(int,input().split()))+[0]
    b=[0]*(m+2)
    ls.append(a)
    pp.append(b)
ls.append([0]*(m+2))
pp.append([0]*(m+2))
# print(ls)
# print(pp)
for i in range(1,n+1):
    for j in range(1,m+1):
        if ls[i-1][j]==1: #上
            pp[i][j]+=1
        if ls[i+1][j]==1:
            pp[i][j]+=1
        if ls[i][j-1]==1:
            pp[i][j]+=1
        if ls[i][j+1]==1:
            pp[i][j]+=1
        if ls[i+1][j+1]==1:
            pp[i][j]+=1
        if ls[i-1][j-1]==1:
            pp[i][j]+=1
        if ls[i+1][j-1]==1:
            pp[i][j]+=1
        if ls[i-1][j+1]==1:
            pp[i][j]+=1


for i in range(1,n+1):
    for j in range(1,m+1):
        if ls[i][j]==1:
            pp[i][j]=9

for k in pp[1:n+1]:
    for l in k[1:m+1]:
        print(l,end=' ')
    print()

