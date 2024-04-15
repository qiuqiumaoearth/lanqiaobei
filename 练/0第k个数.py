n,k=map(int,input().split())
shu=[]
for i in range(1,n+1):
    # a=0
    # for j in str(i):
    #     a+=int(j)
    if i<10:
        shu.append([i,i])
    else:
        shu.append([i,i%10+1])
#print(shu)
shu.sort(key=lambda x:x[1])
#print(shu)
print(shu[k-1][0])