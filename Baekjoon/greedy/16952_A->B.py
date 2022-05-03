a, b = map(int, input().split())
count = 1

while b > a:
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 1:
        break
    else:
        b //= 2
    count += 1

if b == a:
    print(count)
else:
    print(-1)