import re
n = int(input())
li = []

for _ in range(n):
    line = input()
    li += re.compile('[0-9]+').findall(line)

for l in sorted(list(map(int, li))):
    print(l)