n = int(input())
m = 2
while n > 1:
    if n/m == int(n/m):
        n = n/m
        print(m)
    else:
        m += 1