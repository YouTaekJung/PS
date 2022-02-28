r, c = map(int, input().split())
li = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = True

for _ in range(r):
    li.append(list(input()))

for i in range(r):
    for j in range(c):
        if li[i][j] == 'W':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < r and 0 <= y < c:
                    if li[x][y] == 'S':
                        res = False
                        break
        elif li[i][j] == '.':
            li[i][j] = 'D'

if res:
    print(1)
    for l in li:
        print(''.join(l))
else:
    print(0)