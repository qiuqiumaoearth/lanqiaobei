# import itertools
#
# #用字典描绘相邻元素
# dict={'a':['b','f'],'b':['a','g','c'],'c':['b','g','d'],
#       'd':['c','e'],'e':['d','f','g'],'f':['a','g','e'],
#       'g':['b','c','e','f']}
# s='abcdefg'
# ans=[]
# cnt=0
#
# for i in range(1,8):
#     for j in itertools.combinations(s,i):
#         #conmination  组合
#         ans.append(''.join(j))
#     #print(ans)
#
# for str1 in ans:
#     if len(str1)==1:
#         cnt+=1
#         continue
#     for str2 in itertools.permutations(str1):
#         #permutation 全排序
#         #print(str2)
#         for c in range(1,len(str2)):
#             #print(str2[c-1],end='')
#             if str2[c-1] not in dict[str2[c]]:
#                 break
#         else:
#             cnt+=1
#             break
# print(cnt)
# #
# for i in itertools.permutations()

import itertools

#用字典描绘相邻元素
dict={'a':['b','f'],'b':['a','g','c'],'c':['b','g','d'],
      'd':['c','e'],'e':['d','f','g'],'f':['a','g','e'],
      'g':['b','c','e','f']}
s='abcdefg'
ans=[]
cnt=0
for i in range(1,8):
      for j in itertools.combinations(s,i):
            ans.append('')






