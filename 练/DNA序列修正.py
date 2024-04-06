# n=int(input())
# ls_1=input()
# ls_2=input()
# b=0
# dict={'A':0,'T':0,'G':0,'C':0}
# for i in range(n):
#     #print(ls_1[i],ls_2[i])
#     if ls_1[i]==ls_2[i]:
#         dict[ls_1[i]]+=1
# print(min(dict['A'],dict['T'])+min(dict['G'],dict['C']))
t = int(input())
a = list(input())
b = list(input())
mp = {'A':0 , 'C':1 , 'G':2 , 'T':3}
ans = 0
for i in range(t):
    if mp[a[i]] + mp[b[i]] != 3:
        for j in range(i+1,t):
            if mp[a[i]] + mp[b[j]] == 3 and mp[a[j]] + mp[b[i]] == 3:
                b[i],b[j] = b[j],b[i]
                break
        ans += 1
print(ans)




