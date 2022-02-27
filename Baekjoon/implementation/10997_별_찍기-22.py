n = int(input())

def star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']

    li = star(n - 1)

    li.insert(0, '*' * (4 * n - 3))
    li.insert(1, '*')
    li[2] = '* ' + li[2] + '**'
    li[3] = '* ' + li[3] + ' ' * (4 * n - 7) + '*'
    for i in range(4, 4 * n - 3):
        li[i] = '* ' + li[i] + ' *'
    li.append('*' + ' ' * (4 * n - 5) + '*')
    li.append('*' * (4 * n - 3))
    return li


print('\n'.join(star(n)))