# ls=list(map(int,input().split()))
# if 0 in ls:
#     print(max(ls))
# else:
#     a=min(ls)
#     b=max(ls)
#     print(b+a*2)
#

# def shu(ls):
#     a = min(ls)
#     b = max(ls)
#     ls[0] -= a
#     ls[1] -= a
#     ls[2] -= a
#     ls[3] += a * 2
#     return ls
# ls=list(map(int,input().split()))
# ls.sort()
# shu_1=[]
# while ls.count(0)<=2:
#     a=ls.count(0)
#     if a==1:
#         ls[0]+=2
#         ls[1]-=1
#         ls[2]-=1
#         ls[3]-=1
#         print(ls)
#         ls.sort()
#         shu_1.append(ls[-1])
#     if a==0:
#         ss=shu(ls)
#         shu_1.append(ss[-1])
# print(max(shu_1))
    # if 0 not in ls:
    #     a = min(ls)
    #     b = max(ls)
    #     ls[0] -= a
    #     ls[1] -= a
    #     ls[2] -= a
    #     ls[3] += a * 2


ls=list(map(int,input().split()))
kn=[]
ls.sort()
if 0 not in ls:
        a = min(ls)
        b = max(ls)
        ls[0] -= a
        ls[1] -= a
        ls[2] -= a
        ls[3] += a * 2
kn.append(ls[3])
#print(ls)
#print(kn)
if ls.count(0)==1:
    ls.remove(0)
    kn.append(max(ls))
    kn.append(2**(min(ls)))
print(max(kn))





