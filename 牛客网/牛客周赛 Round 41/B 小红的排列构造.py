# n, k = map(int, input().split())
# ls = list(map(int, input().split()))
#
# # 集合--多少个不同的
# gs = len(set(ls))
#
#
# def gou_zao(s, ci):
#     ji_he = list(set(s))
#     a = s.copy()
#     for i in range(len(s)):
#         if a[i] != a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#
#     return a
#
#
# if k > gs or k % 2 != 0:
#     print('-1')
# else:
#     for j in gou_zao(ls, k):
#         print(j, end=' ')

# n, k = map(int, input().split())
# ls = list(map(int, input().split()))
# if k > n:
#     print('-1')
# else:
#     a = ls[k:]




