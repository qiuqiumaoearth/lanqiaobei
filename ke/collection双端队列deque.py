# from collections import Counter
# a=['a','a','b','c','f','d']
# b=Counter(a)
# print(b)
# for x,y in b.items():
#     print(x,y)
#
# for k in b:
#     print(k)


# #双端队列deque 比list速度快
# from collections import deque
# a=deque([1,2,3,4,5])
# # a.append(1)
# # a.appendleft(0)
# # print('a=',a)
# # a.pop()
# # print('a=',a)
# # a.popleft()
# # print('a=',a)
# # a.extend([6,7,8,9])
# # print('a=',a)
# # a.remove(2)
# # print('a=',a)
# # a.reverse()
# # print(a)
# a.rotate(1)#向右移动一位
# print(a)
# a.rotate(-2)#向左移动两位
# print(a)

#
# from collections import defaultdict  #有默认值的键
# d=defaultdict(list)
# d=defaultdict(dict)
# d=defaultdict(set)
# '''即便里面没有值，也能加入'''


