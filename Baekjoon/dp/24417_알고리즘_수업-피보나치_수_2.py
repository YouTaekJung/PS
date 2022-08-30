n = int(input())
x, y = 1, 1

for _ in range(n-2):
    y, x = (x + y) % 1000000007, y
print(y, n - 2)