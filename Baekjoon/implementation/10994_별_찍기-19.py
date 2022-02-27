n = int(input())

def star(n):
    if n == 1:
        return ['*']

    li = star(n - 1)

    li.insert(0, '*' * (4 * n - 3))
    li.insert(1, '*' + ' ' * (4 * n - 5) + '*')
    for i in range(2, 4 * n - 5):
        li[i] = '* ' + li[i] + ' *'
    li.append('*' + ' ' * (4 * n - 5) + '*')
    li.append('*' * (4 * n - 3))
    return li


print('\n'.join(star(n)))