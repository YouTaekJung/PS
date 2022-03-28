import re
n = int(input())
li = [input() for _ in range(n)]
li.sort(key=lambda x: (len(x), sum(map(int, re.findall("\d", x))), x))

for l in li:
    print(l)
