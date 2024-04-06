n=int(input())
a,b,c=map(int,input().split())
sum=0
for i in range(1,n+1):
    #if a%i!=0 and b%i!=0 and c%i!=0:
    if i%a!=0 and i%b!=0 and i%c!=0:
        #print(i)
        sum+=1
print(sum)