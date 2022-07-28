k = int(input())
size, count = 1, 0

while size < k:
    size <<= 1
ans = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(ans, count)