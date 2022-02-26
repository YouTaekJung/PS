import math

n, k = map(int, input().split())
li = [[0, 0] for i in range(7)]

for _ in range(n):
    s, g = map(int, input().split())
    li[g][s] += 1

print(sum(list(map(lambda x: math.ceil(x[0] / k) + math.ceil(x[1] / k), li))))