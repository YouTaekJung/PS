n, m = map(int, input().split())
s = set(list(map(int, input().split()))[1:])
party = [set(list(map(int, input().split()))[1:]) for _ in range(m)]

for _ in range(m):
    for p in party:
        if p & s:
            s |= p

ans = 0
for p in party:
    if not p & s:
        ans += 1

print(ans)