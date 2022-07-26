n, k = int(input()), int(input(), 2)
count = 0

while k != 0:
    k = int(bin(k - (k & ((~k) + 1))), 2)
    count += 1

print(count)