n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

li = sorted(li)
for i in range(n):
    print(li[i])