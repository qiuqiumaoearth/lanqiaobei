# 读入数组长度
n = int(input())
# 读入数组
q = list(map(int,input().split()))
# 创建两个有序数组合并后的辅助数组
tmp = [0] * n
ans = 0

def merge_sort(l, r):
    global ans
    # 如果递归到只有一个数字的区间则直接返回
    if l == r:
        return 
    # 取区间中值
    mid = (l + r) // 2
    # 递归左区间
    merge_sort(l,mid)
    # 递归右区间
    merge_sort(mid+1,r)
    # 设置左区间的指针
    i = l
    # 设置右区间的指针
    j = mid + 1
    # 设置合并后的数组的指针
    k = 0
    # 比较左右两个区间
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            # 若左边较小，则将左边指针指向的数字放入新数组
            tmp[k] = q[i]
            k += 1
            i += 1
        else:
            # 若右边较小，则将有边指针指向的数字放入新数组
            tmp[k] = q[j]
            k += 1
            j += 1
            # 计算逆序对
            ans += mid - i + 1
    # 若左区间还有数组，则依次放入新数组中
    while i <= mid:
        tmp[k] = q[i]
        k += 1
        i += 1
    # 若右区间还有数组，则依次放入新数组中
    while j <= r:
        tmp[k] = q[j]
        k += 1
        j += 1
    j = 0
    # 将辅助数组的中的值（即为最后排好序的值）以此放入原本的区间中
    for i in range(l,r+1):
        q[i] = tmp[j]
        j += 1

merge_sort(0,n-1)

print(ans)