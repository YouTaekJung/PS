from bisect import bisect_left

n, m, k = map(int, input().split())
li = sorted(list(map(int, input().split())))
check = [0] * m
card = list(map(int, input().split()))

for c in card:
    cur = bisect_left(li, c)
    while check[cur] or li[cur] <= c:
        cur += 1
    print(li[cur])
    check[cur] = 1