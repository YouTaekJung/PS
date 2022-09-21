import sys
input = sys.stdin.readline

n = int(input())
li = sorted([tuple(map(int, input().split())) for _ in range(n)])
check = [list(li[0])]

for i in range(1, n):
    if check[-1][1] >= li[i][0]:
        check[-1][1] = max(check[-1][1], li[i][1])
    else:
        check.append(list(li[i]))

ans = 0
for c in check:
    ans += c[1] - c[0]

print(ans)