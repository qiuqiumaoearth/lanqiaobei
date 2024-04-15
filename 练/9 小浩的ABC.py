import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    if n == 1:
        print(-1)
    elif n <= 1000001:
        print(f"{n-1} 1 1")
    else:
        b = (n - 1) // 1000000
        a = 1000000
        c = n - a * b
        print(f"{a} {b} {c}")


# import sys
# n=int(sys.stdin.readline())
# for _ in range(n):
#     a=int(sys.stdin.readline())
#     if a==1:
#         print(-1)
#     elif a<=1000001:
#         print(f"{a-1} 1 1")
#     else:
#         i=(a-1)//1000000
#         j=1000000
#         k=a-i*j
#         print(f"{i},{j},{k}")