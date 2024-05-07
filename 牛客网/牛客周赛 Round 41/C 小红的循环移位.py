n = input()
a = -2
b = -1
f = 0
if len(n) == 1:
    if n == '0' or n == '4' or n == '8':
        print(1)
    else:
        print('-1')
else:
    for i in range(len(n)):
        c = int(n[a+i]+n[b+i])
        if c % 4 == 0:
            f = 1
            print(i)
            break
    if f == 0:
        print(-1)









# f = 0
# g = 0
# s = n
# for i in range(len(n)):
#     a = int(n)
#     if a % 4 != 0:
#         g += 1
#         n = n[g:] + n[:g]
#     else:
#         print(g)
#         f = 1
#         break
#     n = n[i:]+n[:i]
#
# # print(n)
# if f == 0:
#     print(-1)
