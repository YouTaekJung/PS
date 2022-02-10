import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

li_s = Counter(li).most_common()
print(round(sum(li) / n))
print(li[n // 2])
if len(li_s) > 1 and li_s[0][1] == li_s[1][1]:
    print(li_s[1][0])
else:
    print(li_s[0][0])
print(li[-1] - li[0])