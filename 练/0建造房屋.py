import itertools
ls=['A','B','C','D','E','F']
for i in itertools.combinations(ls,5):
    if 'D' in i or 'E' in i or 'F' in i:
        print(i)