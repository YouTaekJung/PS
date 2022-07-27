n = int(input())
li = list(map(int, input().split()))
s = int(input())
i = n - 2

while i > 1 and s > 0:
    if li[i] < li[i + 1]:
        li[i], li[i + 1] = li[i + 1], li[i]
        i = n - 2
        s -= 1
        continue
    if i == n - 2:
        break
    i -= 1

print(*li)
