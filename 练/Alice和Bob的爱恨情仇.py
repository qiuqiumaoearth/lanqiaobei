n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
if sum_a % 2 == 1:
  print('Alice')
else:
  print('Bob')
