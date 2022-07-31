def power(c, n):
    if n == 1:
        return c
    elif n % 2:
        return multi(power(c, n - 1), c)
    else:
        return power(multi(c, c), n // 2)

def multi(a,b):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % 1000
    return temp

n, b = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
ans = power(c, b)

for a in ans:
    print(*map(lambda x: x % 1000, a))