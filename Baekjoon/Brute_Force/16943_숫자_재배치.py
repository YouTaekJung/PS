from itertools import permutations

a, b = input().split()
c = -1

li = list(map(lambda x: ''.join(x), permutations(a)))

for l in li:
    if l[0] == '0':
        continue
    l = int(l)
    if l < int(b):
        c = max(c, l)

print(c)
