n = int(input())

def star(n):
    if n == 0:
        return ['*']

    stars = star(n // 2)
    li = ['' for _ in range(2*n)]
    print(n, stars, li)
    for i in range(len(stars)):
        c = stars[i].count('*')
        li[2 * i] += '**' * c
        li[2 * i + 1] += '* ' * (c - 1) + '*'
    print(li)
    return li


print('\n'.join(star(n)))