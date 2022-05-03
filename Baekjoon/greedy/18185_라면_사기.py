n = int(input())
li = list(map(int, input()[::-1].split()))

def check(li):
    ans = 0
    for i in range(n - 2):
        if li[i] > 0 and i + 2 < n:
            m = min(li[i], li[i + 1], li[i + 2])
            li[i] -= m
            li[i + 1] -= m
            li[i + 2] -= m
            ans += 7 * m
    for i in range(n - 1):
        if li[i] > 0 and i + 1 < n:
            m = min(li[i], li[i + 1])
            li[i] -= m
            li[i + 1] -= m
            ans += 5 * m
    for i in range(n):
        if li[i] > 0 and i < n:
            m = li[i]
            li[i] -= m
            ans += 3 * m
    return ans

print(min(check(li[:]), check(li[::-1])))