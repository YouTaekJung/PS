a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
ans = 0
for i in b:
    ans += a // i
    a %= i
print(ans)