n, k = map(int, input().split())
if k == 1 or n < k:
    print(-1)
else:
    l = input().split()
    l = l[1:k] + [l[0]] + l[k:]
    print(*l)
