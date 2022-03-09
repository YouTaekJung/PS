a, b = map(int, input().split())

li = []
n = 1
while len(li) < b:
    for i in range(n):
        li.append(n)
    n += 1

print(sum(li[a-1:b]))
