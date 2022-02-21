n = int(input())
f = int(input())
res = n // 100 * 100

while res % f != 0:
    res += 1
print(str(res)[-2:])