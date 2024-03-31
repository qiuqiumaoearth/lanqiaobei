#堆的概念
'''堆是特殊的完全二叉树   每个节点都有对应下标
左子节点 2K+1
右子节点 2K+2'''

import heapq
a=[11,6,9,8,7,3]

heapq.heapify(a)
print(a)

heapq .heappush(a,5)
print(a)
while len(a):
    print(heapq.heappop(a),end='')