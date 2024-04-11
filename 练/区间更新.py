from itertools import accumulate
while True:
    try:
        n,m=map(int,input().split())
        ls=list(map(int,input().split()))
        cf_ls=[0]*(n+1)
        cf_ls[0]=ls[0]
        for i in range(1,n):
            cf_ls[i]=ls[i]-ls[i-1]
        for j in range(m):
            x,y,z=map(int,input().split())
            cf_ls[x-1]+=z
            cf_ls[y]-=z

        ls[0]=cf_ls[0]
        for k in range(1,n):
            ls[k]=ls[k-1]+cf_ls[k]
        print(" ".join((map(str,ls))))
        # jie=list(accumulate(cf_ls))
        # for k in jie[:-1]:
        #     print(k,end=' ')
    except:
        break
