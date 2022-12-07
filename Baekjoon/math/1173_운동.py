N, m, M, T, R = map(int, input().split())
count = t = 0
cur = m
while count < N:
    if m+T > M:
        break
    if cur + T <= M:
        cur += T
        count += 1
    else:
        cur = max(cur - R, m)
    t += 1
print(t if count == N else -1)