from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
li_a = list(map(int, input().split()))
m = int(input())
li_b = list(map(int, input().split()))

def sum_li(li):
    res = []
    for i in range(len(li)):
        acc = 0
        for j in range(i, len(li)):
            acc += li[j]
            res.append(acc)
    return res

s_a, s_b = sorted(sum_li(li_a)), sorted(sum_li(li_b))

ans = 0
for s in s_a:
    left = bisect_left(s_b, t - s)
    right = bisect_right(s_b, t - s)
    if left < len(s_b) and s_b[left] == t - s:
        ans += right - left
print(ans)