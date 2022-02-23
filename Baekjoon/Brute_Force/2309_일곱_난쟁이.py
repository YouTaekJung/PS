li = []

for _ in range(9):
    li.append(int(input()))

li.sort()
s = sum(li)
flag = 1
for i in range(9):
    for j in range(i + 1, 9):
        if s - li[i] - li[j] == 100 and flag == 1:
            flag = 0
            res = li[0:i] + li[i+1:j] + li[j+1:]
            for r in res:
                print(r)