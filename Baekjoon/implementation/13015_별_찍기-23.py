n = int(input())

for i in range(2 * n - 1):
    if i == 0 or i == 2 * (n - 1):
        print('*' * n + ' ' * (2 * n - 3) + '*' * n)
    elif i == n - 1:
        print(' ' * i + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) +'*')
    else:
        print(' ' * min(2 * n - i - 2, i) + '*' + ' ' * (n - 2) + '*', end='')
        print(' ' * (abs(n - 1 - i) * 2 - 1) + '*' + ' ' * (n - 2) + '*')
