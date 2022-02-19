n = int(input())
li = [0] + list(map(int, input().split()))
m = int(input())

for _ in range(m):
    g, c = map(int, input().split())
    if g == 1:
        temp = c
        while temp <= n:
            li[temp] = abs(li[temp] - 1)
            temp += c
    else:
        i = 0
        while 1 <= c - i and c + i <= n and li[c + i] == li[c - i]:
            i += 1
        i -= 1
        for j in range(c - i, c + i + 1):
            li[j] = abs(li[j] - 1)

for i in range(1, n, 20):
    print(*li[i:i+20])