ls=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
qv_ls=[]
for _ in range(4):
    qv_ls.append([0]*4)

qv_ls[0][0]=ls[0][0]
print(ls)
print(qv_ls)

for i in range(len(ls)):
    if i==0:
        for j in range(1,len(ls[i])):
            qv_ls[i][j]=ls[i][j]+qv_ls[i][j-1]
    else:
        for j in range(len(ls[i])):
            if j==0:
                qv_ls[i][j]=ls[i][j]+qv_ls[i-1][j]

            else:
                qv_ls[i][j]=qv_ls[i-1][j]+qv_ls[i][j-1]+ls[i][j]-qv_ls[i-1][j-1]

print('当当当，二维前缀和',qv_ls)







