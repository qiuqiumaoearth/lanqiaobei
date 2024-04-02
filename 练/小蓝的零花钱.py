# n,b=map(int,input().split())
# ls=list(map(int,input().split()))
# ji=0
# lp=[]
# for i in range(1,n,2):
#     if i!=n-1:
#         lp.append(abs(ls[i+1]-ls[i]))
# lp.sort()
# print(lp)
# count=0
# for j in lp:
#     if b-j>=0:
#         count+=1
#         b-=j
# print(count)

n,B=map(int,input().split())
ls=list(map(int,input().split()))
dict={'ji':0,"ou":0}
ll=[]
for i in range(n):
    if ls[i]%2==0:
        dict['ou']+=1
    else:
        dict['ji']+=1
    if dict['ji']==dict['ou']:
        if i!=n-1:
            ll.append(abs(ls[i]-ls[i+1]))
        #print('y')
    #print(dict)
#print(ll)
ll.sort()
count=0
for j in ll:
    B-=j
    if B>=0:
        count+=1
print(count)


'''嗷嗷哦嗷嗷，棒棒棒，一遍过'''
