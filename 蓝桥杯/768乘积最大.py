# n=input()
# a=0
# for i in range(1,len(n)):
#     print(int(n[:i]),int(n[i:]))
#     print(int(n[:i])*int(n[i:]))
#
# s,k=map(int,input().split())
# n=int(input())
#
# def fenge(a):
#     a=str(a)
#     x=int(a[0])
#     y=1
#     z=1
#     for i in range(1,len(a)):
#         if x<int(a[:i])*int(a[i:]):
#             x=int(a[:i])*int(a[i:])
#     return x,int(a[:i]),int(a[i:])
#
# ls=[n]
# for i in range(k):
#     p = ls.pop(-1)
#     print(p)
#     ll=fenge(p)
#     ls.append(ll[1])
#     ls.append(ll[2])
#     ls.sort()
#     ls.reverse()
# print(ls)
# sum=1
# for j in ls:
#     sum*=j
# print(sum)




#啊啊啊啊啊啊啊啊啊啊啊啊啊啊
'''笨比 直接用库不就行了'''
import itertools
n,k=map(int,input().split())
s=['A','B','C']
for i in itertools.combinations(s,k):
    print(i)