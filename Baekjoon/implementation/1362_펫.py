ans = 0
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break

    flag = False
    while True:
        action, n = input().split()
        if action == '#' and n == '0':
            break

        if not flag:
            n = int(n)
            if action == 'E':
                w -= int(n)
            elif action == 'F':
                w += int(n)

        if w <= 0:
            flag = True

    ans += 1
    if w <= 0:
        print(f'{ans} RIP')
    elif o / 2 < w < o * 2:
        print(f'{ans} :-)')
    else:
        print(f'{ans} :-(')