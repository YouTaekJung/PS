n = int(input())
li = sorted([input()[0] for _ in range(n)])
s = set(li)
ans = []

for c in s:
    if li.count(c) >= 5:
        ans.append(c)

print(''.join(sorted(ans)) if len(ans) > 0 else "PREDAJA")