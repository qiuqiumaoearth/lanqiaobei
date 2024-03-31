# count=0
# for j in range(12345678,98765432):
#     n=str(j)
# #n=input()
#
#     if '2023' in n:
#         print('yyyyy')
#     a,b,c,d=0,0,0,0
#     for i in n:
#         if i=='2':
#             a=1
#         if i=='0' and a==1:
#             b=1
#         if i=='2' and a==1 and b==1:
#             c=1
#         if i=='3' and a==1 and b==1 and c==1:
#             d=1
#             print('YES')
#             count+=1
#             print(count)
#             break
#
#     print(count)
#最后的count结果式460725

print(98765432-12345678-460725)





    # print(j,count)
#
#
# # import re
# #
# # pat = re.compile(r'\d*'.join('2023'))
# # nums = range(12345678, 98765432 + 1)
# # print(sum(not re.search(pat, i) for i in map(str, nums)))
#
#
#
# # for i in range(12345678,98765432):
# #     a=str(i)
# #     for j in a:
# #         if j==temp[x]:
# #             x+=1
# #         if x==4:
# #             ans+=1
# #             #print(ans)
#         break
#
# ans = 0
#
#
# def find(x):
#     tmp = "2023"
#     a = str(x)
#     j = 0
#     for i in a:  # 对数字进行遍历
#         if i == tmp[j]:  # 从左到右逐个遍历是否依次会出现2023四个数字
#             j += 1
#         if j == 4:  # 说明完全包含2023
#             return True
#     return False
#
# for i in range(12345678, 98765433):
#     if not find(i):  # 注意这里要的是完全不包含2023，
#         ans += 1  # 要取反加not，我这里没仔细看，结果就是反向答案
#     print(ans)
#
# # print(98765433 -12345678 - 460725) # 用反向答案求答案。。。
#
# # 反向答案 460725
# # 答案 85959030



