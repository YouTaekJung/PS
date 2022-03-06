from itertools import combinations
first = 1

while True:
    temp = list(map(int, input().split()))
    if temp == [0]:
        break
    else:
        if first != 1:
            print()
        first = 0
        n, li = temp[0], temp[1:]
        com = list(combinations(li, 6))
        for c in com:
            print(*c)