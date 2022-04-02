n = int(input())
num_li = list(map(int, input().split()))
m = int(input())
li = list(map(int, input().split()))
d = {}

for num in num_li:
    d[num] = d.get(num, 0) + 1

print(*list(map(lambda x: d.get(x, 0), li)))
