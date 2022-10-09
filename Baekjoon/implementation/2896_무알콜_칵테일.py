a, b, c = map(int, input().split())
l, j, k = map(int, input().split())
m = min(a / l, b / j, c / k)
print(a - l * m, b - j * m, c - k * m)