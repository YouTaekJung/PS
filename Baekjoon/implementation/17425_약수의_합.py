import sys
dp = [0 for _ in range(1000001)]

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        cache[j] += i
    cache[i] += cache[i-1]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(cache[n])