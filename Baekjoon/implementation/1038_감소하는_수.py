from itertools import combinations

n = int(input())
li = []
for i in range(1, 11):
    for com in combinations(range(10), i):
        com = sorted(list(com), reverse=True)
        li.append(int("".join(map(str, com))))
li.sort()

print(li[n] if len(li) > n else -1)