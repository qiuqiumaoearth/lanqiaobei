def han(n):
    if n==1:
        return 1
    else:
        return 2*han(n-1)+1
print(han(int(input())))