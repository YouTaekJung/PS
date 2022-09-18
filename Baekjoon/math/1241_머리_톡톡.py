import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
ans = [0] * n
check = [0] * (max(li) + 1)

for l in li:
    check[l] += 1

for i in range(n):
    p = 1
    while p ** 2 <= li[i]:
        if not li[i] % p:
            if p ** 2 != li[i]:
                ans[i] += check[p] + check[li[i] // p]
            else:
                ans[i] += check[p]
        p += 1

for a in ans:
    print(a - 1)