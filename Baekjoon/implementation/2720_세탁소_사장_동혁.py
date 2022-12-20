money = [25, 10, 5, 1]
ans = [0] * 4

for _ in range(int(input())):
    cur = int(input())
    for i, m in enumerate(money):
        ans[i] = cur // m
        cur %= m

    print(' '.join(map(str, ans)))