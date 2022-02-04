n = int(input())

li = []
for _ in range(n):
    li.append(input())

li = list(set(li))
li = sorted(li)
li = sorted(li, key = lambda x: len(x))

for i in range(len(li)):
    print(li[i])