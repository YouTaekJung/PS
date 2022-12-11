s, n, k, r1, r2, c1, c2 = map(int, input().split())
board = []

def recur(size, point):
    x, y = point
    c = size // n
    if size == 1:
        return 0
    if c * (n - k) // 2 <= x < c * (n + k) // 2 and \
        c * (n - k) // 2 <= y < c * (n + k) // 2:
        return 1
    x, y = [x % c, y % c]
    return recur(size // n, [x, y])

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(recur(n ** s, [i, j]), end="")
    print()
