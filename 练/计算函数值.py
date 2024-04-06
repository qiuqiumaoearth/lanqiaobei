def s(n):
    if n==0:
        return 1
    if n%2==0:
        return s(n/2)
    if n%2!=0:
        return s(n-1)+1
a=int(input())
print(s(a))
