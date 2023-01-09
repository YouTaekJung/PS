ms = input()
n = int(input())
li = sorted([input() for i in range(n)])
mp = mi = 0
for i in range(n):
    L = ms.count("L") + li[i].count("L")
    O = ms.count("O") + li[i].count("O")
    V = ms.count("V") + li[i].count("V")
    E = ms.count("E") + li[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if mp < p:
        mp = p
        mi = i
print(li[mi])