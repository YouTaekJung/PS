import sys
input = sys.stdin.readline

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


n, m = map(int, input().split())
li = [0 for _ in range(n)]
tree = [0] * 4 * n

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n - 1, 1, b - 1, c - li[b - 1])
        li[b - 1] = c
    else:
        if b > c:
            b, c = c, b
        print(interval_sum(0, n - 1, 1, b - 1, c - 1))