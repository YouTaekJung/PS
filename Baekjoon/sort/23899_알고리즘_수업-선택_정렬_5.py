n = int(input())
li = list(map(int, input().split()))
match = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    idx = li.index(max(li[:i + 1]))
    if idx != i:
        li[idx], li[i] = li[i], li[idx]
        if li == match:
            print(1)
            exit()
print(0)