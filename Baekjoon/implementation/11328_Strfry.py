n = int(input())

for _ in range(n):
    x, y = input().split()
    if sorted(x) == sorted(y):
        print('Possible')
    else:
        print('Impossible')