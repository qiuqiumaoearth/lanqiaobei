# n=int(input())
# ls=list(map(int,input().split()))
# ll=[0]*(n+2)
# for i in range(n):
#     a=ll[i]+ll[i+1]+ll[i+2]
#     if ls[i]>a:
#         if ls[i]-a==1:
#             ll[i+2]=1
# if ll[-1]==1:
#     ll[-2]=1
# print(ll)
# for j in ll[1:n+1]:
#     print(j,end=' ')
#


# def solve_linear_equations(n, a):
#     result = [0] * (n + 1)
#     result[1] = a[0] % 2
#     for i in range(2, n + 1):
#         if a[i - 1] % 2 == 0:
#             result[i] = result[i - 2]
#         else:
#             result[i] = 1 - result[i - 2]
#     return result[1:]
#
# # 读取输入
# n = int(input())
# a = list(map(int, input().split()))
#
# # 解决方程组并输出结果
# solution = solve_linear_equations(n, a)
# print(" ".join(map(str, solution)))


n = int(input())
ls = list(map(int, input().split()))
ll = [0] * (n + 2)

for i in range(n):
    a = ll[i] + ll[i + 1] + ll[i + 2]
    if ls[i] > a:
        if ls[i] - a == 1:
            ll[i + 2] = 1
        elif ls[i] - a == 2:
            ll[i + 1] = 1
            ll[i + 2] = 1
        elif ls[i] - a == 3:
            ll[i] = 1
            ll[i + 1] = 1
            ll[i + 2] = 1
print(ll)
