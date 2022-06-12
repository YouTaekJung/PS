w, h, x, y, p = map(int, input().split())
ans = 0
for _ in range(p):
    nx, ny = map(int, input().split())
    if (x <= nx <= x + w and y <= ny <= y + h) or \
        (nx < x and (nx - x) ** 2 + (ny - y - h/2) ** 2 <= (h / 2) ** 2) or \
        (nx > x + w and (nx - x - w) ** 2 + (ny - y - h/2) ** 2 <= (h / 2) ** 2):
        ans += 1
print(ans)