n = int(input())

def star(n):
    if n == 1:
        return ['*']

    stars = star(n // 2)
    li = []

    for s in stars:
        li.append(' ' * n + s * 1)
    for s in stars:
        li.append(' ' * (n - 1) + s + ' ' * (n // 2) + s)
    for s in stars:
        li.append(' ' * (n - 2) + s * 5)
    return li


print('\n'.join(star(n // 3)))