import sys
input = sys.stdin.readline

n, q = map(int, input().split())
check = [0] * (n + 1)

for _ in range(q):
    ans = 0
    cur = start = int(input())
    while cur >= 1:
        if check[cur] == 1:
            ans = cur
        cur //= 2
    check[start] = 1
    print(ans)