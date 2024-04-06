# def shu(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 0
#     if n>1:
#         return shu(n-1)+1
# print(shu(int(input())))


import os
import sys


n = int(input())
def find(num) :
  res = 1
  mid = num // 2
  if mid != 0 :
    for i in range (1,mid + 1) :
      res += find(i)
  else :
    return 1
  return res
print(find(n))