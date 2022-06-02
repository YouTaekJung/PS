n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li += [li[0]]
ans = 0

for i in range(n):
    [x1, y1], [x2, y2] = li[i], li[i + 1]
    ans += x1 * y2 - x2 * y1

print(round(abs(ans) / 2, 1))