n = int(input())
li = []
res = 0

for i in range(n):
    li.append(int(input()))
li.sort()

for i in range(n):
    li[i] *= (n - i)
print(max(li))