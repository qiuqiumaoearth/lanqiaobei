a=list(input())
b=list(input())
zhuo=[]
while len(a)!=0 and len(b)!=0:
    a_c=a.pop(0)
    if a_c not in zhuo:
        zhuo.append(a_c)
    else:
        wz=zhuo.index(a_c)
        zhuo.append(a_c)
        c=zhuo[wz:]
        c.reverse()
        a=a+c
        zhuo=zhuo[:wz]
    print('a 的牌{}'.format(a))
    print('桌面上的牌{}'.format(zhuo))
    b_c=b.pop(0)
    if b_c not in zhuo:
        zhuo.append(b_c)
    else:
        wz = zhuo.index(b_c)
        zhuo.append(b_c)
        c = zhuo[wz:]
        c.reverse()
        b = b + c
        zhuo = zhuo[:wz]
    print('b 的牌{}'.format(b))
    print('桌面上的牌{}'.format(zhuo))