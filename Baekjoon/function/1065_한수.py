n = int(input())

if n < 100:
    print(n)
else:
    i = 100
    c = 99
    while i <= min(n, 999):
        d = (i // 100) - (i // 10 % 10)
        if (i // 10 % 10 - i % 10) == d:
            c += 1
        i += 1
    print(c)