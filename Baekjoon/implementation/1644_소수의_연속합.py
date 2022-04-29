n = int(input())
li = [False] * 2 + [True] * (n - 1)
left, right = 2, 2
acc = left
ans = 0

for i in range(2, n + 1):
    for j in range(2 * i, n + 1, i):
        if li[j]:
            li[j] = False

def find_next(num):
    while num < n:
        num += 1
        if li[num]:
            return num
    return False

while left <= right:
    if acc == n:
        ans += 1
        right = find_next(right)
        acc += right
    elif acc < n:
        right = find_next(right)
        acc += right
    else:
        acc -= left
        left = find_next(left)
    if not left or not right:
        break

print(ans)