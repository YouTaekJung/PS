import math
from collections import Counter

li = list(map(int, list(input().replace('9', '6'))))
c = Counter(li).most_common()

if c[0][0] == 6:
    if len(c) == 1:
        print(math.ceil(c[0][1] / 2))
    else:
        print(max(math.ceil(c[0][1] / 2), c[1][1]))
else:
    print(c[0][1])