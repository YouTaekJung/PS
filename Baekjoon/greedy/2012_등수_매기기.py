n = int(input())
li = []
res = 0

for _ in range(n):
    li.append(int(input()))

li.sort()
for i in range(n):
    res += abs(li[i] - (i + 1))

print(res)