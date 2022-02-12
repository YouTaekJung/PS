n = int(input())

li = []
for _ in range(n):
    li.append(input())

res = list(li[0])
for i in range(len(res)):
    for j in range(1, n):
        if res[i] != li[j][i]:
            res[i] = '?'
            break

print(''.join(res))