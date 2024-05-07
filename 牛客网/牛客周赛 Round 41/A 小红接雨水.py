a, b, c = map(int, input().split())
ab = a - b
bc = c - b
kk = min(ab, bc)
if kk < 0:
    print(0)
else:
    print(kk)
