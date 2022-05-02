n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

def check(a, b, s):
    global ans

    num = matrix[a][b]
    for i in range(a, a + s):
        for j in range(b, b + s):
            if matrix[i][j] != num:
                for x in range(3):
                    for y in range(3):
                        check(a + x * s // 3, b + y * s // 3, s // 3)
                return
    ans[num + 1] += 1

check(0, 0, n)
for a in ans:
    print(a)
