# a='abcdabcd'
# b=a.count('abcd')
# print(b)

zfc=input()
ge=[]
for i in range(1,len(zfc)+1):
    ge.append(zfc.count(zfc[:i]))
print(max(ge))
