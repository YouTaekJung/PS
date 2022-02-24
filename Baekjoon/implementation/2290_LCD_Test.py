s, n = input().split()
s = int(s)
res = [[] for _ in range(2 * s + 3)]

for i, num in enumerate(n):
    if num in ['1', '4']:
        res[0] += [' ' * (s + 2)]
    else:
        res[0] += [' ', '-' * s, ' ']

    for i in range(1, s + 1):
        if num in ['1', '2', '3', '7']:
            res[i] += [' ' * (s + 1), '|']
        elif num in ['5', '6']:
            res[i] += ['|', ' ' * (s + 1)]
        else:
            res[i] += ['|', ' ' * s, '|']

    if num in ['1', '7', '0']:
        res[s + 1] += [' ' * (s + 2)]
    else:
        res[s + 1] += [' ', '-' * s, ' ']

    for i in range(s + 2, 2 * s + 2):
        if num in ['1', '3', '4', '5', '7', '9']:
            res[i] += [' ' * (s + 1), '|']
        elif num == '2':
            res[i] += ['|', ' ' * (s + 1)]
        else:
            res[i] += ['|', ' ' * s, '|']

    if num in ['1', '4', '7']:
        res[2 * s + 2] += [' ' * (s + 2)]
    else:
        res[2 * s + 2] += [' ', '-' * s, ' ']

    if i != len(n) - 1:
        for j in range(len(res)):
            res[j] += ' '
for r in res:
    print(''.join(r))
