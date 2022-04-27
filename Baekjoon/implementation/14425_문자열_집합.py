import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
count = 0

for _ in range(n):
    d[input()] = 1

for _ in range(m):
    if input() in d:
        count += 1

print(count)