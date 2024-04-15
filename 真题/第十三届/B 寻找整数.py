# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     a=max(n,m)
#     flag=0
#     for i in range(2,a+1):
#         if i%n==i%m:
#             #print(2%1)
#             print(i)
#             flag=1
#             break
#     if flag==0:
#         print('No')
#     else:
#         print('Yes')
#
#
#

# for i in range(100,100000000):
#     if i%49==46 and i%48==41 and i%47==5 and i%46==15 and i%45==29:
#         print(i)
#         break
#     else:
#         print(1)

#2153

#4772009
# a=4772009
# ls=[1,2,1,4,5,4,1,2,9,0,5,10,11,14,9]
# for i in range(2,17):
#     if a%i!=ls[i-2]:
#         print(i,'no')
#     else:
#         print(1)


a=4772009
for i in range(a,10**12):
    if i%49==46 and i%48==41 and i%47==5 and i%46==15 and i%45==29 and i%44==33 and i%43==11 and i%42==11:
        print(i)
        break
    else:
        print(1)
