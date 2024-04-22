# n,a,b=map(int,input().split())
# ls=list(map(int,input().split()))
# ls.sort()
# r=n-1
# l=0
# #ky=[]
# ans_1=0
# while l<r:
#     if ls[r]+ls[l]<=b :
#         #ky.append([l,r])
#         ans_1+=(r-l)
#         l+=1
#     else:
#         r-=1
#
# r=n-1
# l=0
# ans_2=0
# while l<r:
#     if ls[r]+ls[l]<a :
#         #ky.append([l,r])
#         ans_2+=(r-l)
#         l+=1
#     else:
#         r-=1
# print(ans_1-ans_2)


#
# n,a,b=map(int,input().split())
# ls=list(map(int,input().split()))
# ls.sort()
# l=0
# r=n-1
# ans_1=0
# while l<r:
#     if ls[l]+ls[r]<=b:
#         ans_1+=r-l
#         l+=1
#     else:
#         r-=1
#
# l=0
# r=n-1
# ans_2=0
# while l<r:
#     if ls[l]+ls[r]<a:
#         ans_2+=r-l
#         l+=1
#     else:
#         r-=1
# print(ans_1-ans_2)



def shu(ls,p):
    l=0
    r=len(ls)-1
    ans=0
    while l<r:
        if ls[l]+ls[r]<=p:
            ans+=r-l
            l+=1
        else:
            r-=1
    return ans

n,a,b=map(int,input().split())
ls=list(map(int,input().split()))
ls.sort()
print(shu(ls,b)-shu(ls,a-1))







