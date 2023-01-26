n, m, l = map(int, input().split())
li = [0] * n
count = i = 0
while li[i] < m - 1:
    li[i] += 1
    count += 1
    i = (i + l) % n if li[i] % 2 == 1 else (i - l) % n
print(count)