a, b = map(int, input().split())
if b > 44:
    print(a, b-45)
elif b <= 44 and a >= 1:
    print(a-1, b+15)
else:
    print(23, b+15)