n, m = map(int, input().split())
li = list(map(int, input().split()))
start, end, acc, count = 0, 1, li[0], 0

if acc == m:
    count += 1

while not (start == end == n):
    if acc < m and end < n:
        acc += li[end]
        end += 1
    else:
        acc -= li[start]
        start += 1

    if acc == m:
        count += 1

print(count)