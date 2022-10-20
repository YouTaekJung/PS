n = int(input())
ans = [0] * 10

for i in range(len(str(n))):
    left = 9 - int(str(n)[-1])
    for j in range(len(ans)):
        ans[j] += (n // 10 + 1) * (10 ** i)
    for j in range(10 - left, 10):
        ans[j] -= (10 ** i)
    for num in list(str(n)[:-1]):
        ans[int(num)] -= left * (10 ** i)
    ans[0] -= (10 ** i)
    n //= 10

print(*ans)