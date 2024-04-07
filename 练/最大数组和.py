for _ in range(int(input())):
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
    sum_1=sum(ls)
    ls.sort()
    for i in range(k):
        xiao=ls[0]+ls[1]
        da=ls[-1]
        if xiao>=da:
            sum_1-=da
            ls.pop(-1)
        else:
            sum_1-=xiao
            ls.pop(1)
            ls.pop(0)
    print(ls)
