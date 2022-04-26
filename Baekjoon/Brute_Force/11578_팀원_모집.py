from itertools import combinations

n, m = map(int, input().split())
li = []

for _ in range(m):
    li.append(list(map(int, input().split()))[1:])

def comb():
    for i in range(1, min(11, n + 1)):
        com = list(combinations(li, i))
        for c in com:
            if len(set(range(1, n + 1)) - set(sum(c, []))) == 0:
                return i
    return -1

print(comb())
