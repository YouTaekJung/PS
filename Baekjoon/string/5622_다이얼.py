li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alp = input()
res = 0

for s in alp:
    for i in range(len(li)):
        idx = li[i].find(s)
        if idx >= 0:
            res += i + 3
            break
print(res)