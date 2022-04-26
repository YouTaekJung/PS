a, b = map(int, input().split())
n = int(input())
li = list(map(int, input().split()))
ans = []
num = 0
for i in range(n):
    num += a ** (n - i - 1) * li[i]

m = 1
while b ** m < num:
    m += 1

for i in range(m):
    ans.append(num // b ** (m - i - 1))
    num %= b ** (m - i - 1)

print(*ans)