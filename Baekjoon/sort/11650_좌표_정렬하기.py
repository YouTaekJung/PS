n = int(input())

li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li = sorted(li, key= lambda x: x[1])
li = sorted(li, key= lambda x: x[0])

for i in range(n):
    print(*li[i])