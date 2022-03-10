from itertools import combinations, chain

word = input()
arr = []
res = set()

for i, w in enumerate(word):
    if w == '(':
        arr.append([i, 0])
    elif w == ')':
        j = -1
        while arr[j][1] != 0:
            j -= 1
        arr[j][1] = i

for i in range(1, len(arr) + 1):
    com = list(combinations(arr, i))
    for c in com:
        c = list(chain(*c))
        temp = ''
        for j, w in enumerate(word):
            if j not in c:
                temp += w
        res.add(temp)

res = list(res)
res.sort()
for r in res:
    print(r)