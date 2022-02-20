n, m = map(int, input().split())
li = []
check_x = [0] * m
check_y = [0] * n
for _ in range(n):
    li.append(input())

for i in range(n):
    for j in range(m):
        if li[i][j] == 'X':
            check_x[j] = 1
            check_y[i] = 1

print(max(check_x.count(0), check_y.count(0)))