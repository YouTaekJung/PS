n, w, h = map(int, input().split())
t = (w ** 2 + h ** 2) ** 0.5

for _ in range(n):
    c = int(input())
    print('DA' if c <= t else 'NE')
