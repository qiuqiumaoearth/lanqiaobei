n=int(input())
zhu=list(map(int,input().split()))
oj=[]
jj=[]
for i in range(n):
    if i%2==0:
        oj.append(abs(zhu[i]))
    else:
        jj.append(abs(zhu[i]))
# print('偶＋',oj)
# print('奇-',jj)
if n==1:
    print(abs(zhu[0]))
else:

    a=min(oj)
    b=max(jj)
    if a<b:
        oj.remove(a)
        oj.append(b)
        jj.remove(b)
        jj.append(a)

    # print('偶＋',oj)
    # print('奇-',jj)
    oj_sum=sum(oj)
    jj_sum=sum(jj)
    sum=oj_sum-jj_sum
    print(sum)

