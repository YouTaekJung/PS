def convert(s):
    return [ord(s[0]) - 65, int(s[1]) - 1]

visited = [[0] * 6 for _ in range(6)]
cor = convert(input())
start = cor[:]
visited[cor[0]][cor[1]] = 2

for _ in range(35):
    cur = convert(input())
    x_diff, y_diff = abs(cor[0] - cur[0]), abs(cor[1] - cur[1])
    if visited[cur[0]][cur[1]] or x_diff in [0, 3] or x_diff + y_diff != 3:
        print('Invalid')
        exit()
    visited[cur[0]][cur[1]] = 1
    cor = cur

x_diff, y_diff = abs(cor[0] - start[0]), abs(cor[1] - start[1])
print('Invalid' if x_diff in [0, 3] or x_diff + y_diff != 3 else 'Valid')
