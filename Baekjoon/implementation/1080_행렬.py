def check():
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
ans = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    a[x][y] ^= 1
            ans += 1

print(ans if check() else '-1')