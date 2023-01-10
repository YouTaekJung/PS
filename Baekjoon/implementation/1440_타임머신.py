from itertools import permutations
per = list(permutations(map(int, input().split(":"))))
ans = 0
for a, b, c in per:
    if 1 <= a <= 12 and 0 <= b <= 59 and 0 <= c <= 59:
        ans += 1
print(ans)