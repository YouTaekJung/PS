n, b = map(int, input().split())
res = ''

def base(num):
    if num < 10:
        return str(num)
    else:
        return chr(55 + num)

while n > 0:
    res = base(n % b) + res
    n //= b

print(res)