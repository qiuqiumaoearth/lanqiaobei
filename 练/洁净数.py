n=int(input())
sum=0
for i in range(1,n+1):
    a=list(str(i))
    if '2' not in a:
        sum+=1
print(sum)
