import sys
n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

for l in sorted(li, reverse=True):
    print(l)