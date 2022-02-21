res = 0

for i in range(8):
    r = input()
    if i % 2:
        res += r[1::2].count('F')
    else:
        res += r[::2].count('F')

print(res)