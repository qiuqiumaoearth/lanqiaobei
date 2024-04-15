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