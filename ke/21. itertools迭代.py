import itertools迭代
# a=[1,2,3,4,5]
# b=list(itertools.accumulate(a))
# # for x in b:
# #     print(x)  #前缀和
# print(b)

# a=[3,1,9,2,5]
# b=list(itertools.accumulate(a,max))
# print(b)  #这个列表到这个数之前的最大值
# #[3, 3, 9, 9, 9]

#排列组合
# from itertools import permutations
# a=list(permutations([1,2,3,4]))
# print(a)

# import itertools
# a=[1,2,3,4]
# for x in itertools.combinations(a,2):
#     print(x)

import itertools
a=[1,2,3]
for x in itertools.combinations(a,2):
    print(x)
