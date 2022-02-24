m, n = map(int, input().split())
gcd = 1

for i in range(2, min(m, n) + 1):
    if m % i == 0 and n % i == 0:
        gcd = i

print(gcd)
print(m * n // gcd)