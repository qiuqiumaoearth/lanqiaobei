n=int(input())
ls=[]
for i in range(n):
    a=input()
    ls.append([a,int(a)])
#print(ls)
ls.sort(key=lambda x:x[1])

for j in range(n):
    print(ls[j][0],end='')