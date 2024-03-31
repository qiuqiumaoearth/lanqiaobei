yue=[1,2,3,4,5,6,7,8,9,10,11,12]
ri=[31,28,31,30,31,30,31,31,30,31,30,31]

t_y=0
t_r=0

ans=0

dui_1='012'
dui_2='123'
for i in range(1,13):
    if i<10:
        t_y='0'+str(i)
    else:
        t_y=str(i)
    for j in range(1,ri[i-1]+1):
        if j<10:
            t_r='0'+str(j)
            tt=t_y+t_r
            if (tt[:3] ==dui_1 or tt[1:]==dui_1 or
                    tt[:3] ==dui_2 or tt[1:]==dui_2) :
                ans+=1

        else:
            t_r=str(j)
            tt=t_y+t_r
            if (tt[:3] == dui_1 or tt[1:] == dui_1 or
                    tt[:3] == dui_2 or tt[1:] == dui_2):
                ans += 1
            #if tt[0:3] in dui or tt[1:4] in dui:


    print(ans)