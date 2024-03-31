# n=int(input())
# ls=list(map(int,input().split()))
# temp=[0]*n
# ans=0
#
# def merge_sort(l,r):
#     global ans
#     if l==r:
#         return
#     mid=(l+r)//2
#     #取中间进行分治
#     merge_sort(l,mid)
#     merge_sort(mid+1,r)
#
#     i=l
#     j=mid+1
#     k=0
#
#     while i<=mid and j<=r:
#         if ls[i]<=ls[j]:
#             temp[k]=ls[i]
#             k+=1
#             i+=1
#         else:
#             temp[k]=ls[j]
#             ans+=mid-i+1
#             j+=1
#             k+=1
#     while i<=mid:
#         temp[k]=ls[i]
#         i+=1
#         k+=1
#
#     while j<=r:
#         temp[k]=ls[j]
#         j+=1
#         k+=1
#
#     j=0
#     for i in range(l,r+1):
#         temp[i]=ls[j]
#         j+=1
#
# merge_sort(0,n-1)
#
# print(ans)
#
# #逆序对
#
#
#
# #python 最大10的8次方
# #merge_sort  #归并排序
#



#用归并排序进行数组排列
# n=int(input())
# ls=list(map(int,input().split()))
# l,r=0,n-1
# mid=(l+r)//2
# temp=[0]*n
# j=0
# for i in range(5):
#     if ls[l]<=ls[mid+1]:
#         temp[j]=ls[l]
#         l+=1
#         j+=1
#     else:
#         temp[j]=ls[mid+1]
#         mid+=1
#         j+=1
#     print(temp)

'''5
1 3 6 2 4 5'''

#归并排序
n=int(input())
ls=list(map(int,input().split()))
ans=0
tmp=[0]*n

def merge_sort(l,r):
    global ans
    if l==r:
        return

    mid=(l+r)//2
    merge_sort(l,mid)
    merge_sort(mid+1,r)

    i=l
    j=mid+1
    k=0

    while i<=mid and j<=r:
        if ls[i]<=ls[j]:
            tmp[k]=ls[l]
            k+=1
            i+=1
        else:
            tmp[k]=ls[j]
            ans += mid - i + 1
            k+=1
            j+=1

    while i<=mid:
        tmp[k]=ls[i]
        k+=1
        i+=1

    while j<=r:
        tmp[k]=ls[j]
        k+=1
        j+=1
    j=0
    for i in range(l,r+1):
        ls[i] = tmp[j]
        j += 1
merge_sort(0,n-1)
print(ans)



