n = int(input())

li = []
for _ in range(n):
    li.append(list(input().split()))

li = sorted(li, key=lambda x: int(x[0]))

for l in li:
    print(*l)