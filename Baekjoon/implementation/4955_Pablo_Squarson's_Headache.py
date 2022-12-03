dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
while True:
    n = int(input())
    if not n:
        break
    li = [[0, 0]]
    ans = 1
    for _ in range(n - 1):
        nx, dn = map(int, input().split())
        li.append([li[nx][0] + dx[dn], li[nx][1] + dy[dn]])
    sorted_x = sorted(li, key=lambda x: x[0])
    sorted_y = sorted(li, key=lambda x: x[1])
    print(sorted_y[-1][1] - sorted_y[0][1] + 1, sorted_x[-1][0] - sorted_x[0][0] + 1)