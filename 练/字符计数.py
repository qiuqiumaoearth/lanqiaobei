yuan=['a','e','i','o','u']
n=input()
y=0
f=0
for i in n:
    if i in yuan:
        y+=1
    else:
        f+=1
print(y)
print(f)