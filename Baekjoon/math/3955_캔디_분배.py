t = int(input())

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        n, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - n * x1
        y0, y1 = y1, y0 - n * y1
    return x0, x1, y0, y1

for _ in range(t):
    k, c = map(int, input().split())
    x0, x1, y0, y1 = extended_gcd(c, k)
    if c == 1:
        print('IMPOSSIBLE' if k >= 1e9 else k + 1)
    elif x1 != -k and y1 != -c:
        print('IMPOSSIBLE')
    else:
        ans = x0 if x0 > 0 else x0 + x1
        print('IMPOSSIBLE' if ans > 1e9 else ans)