from itertools import combinations

n = int(input())
li = []
for i in range(1, 11):
    for com in combinations(range(10), i):
        com = sorted(list(com), reverse=True)
        li.append(int("".join(map(str, com))))
li.sort()

print(li[n - 1] if len(li) > n - 1 else -1)