n = int(input())
li = list(map(int, input().split()))

init, check = 1, 0
while init or check != 0:
    init = 0
    i = 0
    check = 0
    while i < n - 1:
        if li[i] + 1 == li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            check += 1
            i += 1
        i += 1

print(*li)
