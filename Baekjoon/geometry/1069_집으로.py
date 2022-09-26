x, y, d, t = map(int, input().split())

ans = distance = (x ** 2 + y ** 2) ** 0.5
q = distance // d
if distance >= d:
    ans = min(ans, q * t + distance % d, (q + 1) * t)
else:
    ans = min(ans, t + (d - distance), 2 * t)
print(ans)