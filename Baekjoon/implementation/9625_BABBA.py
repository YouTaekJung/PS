n = int(input())
res = [0, 1]
count = 1

while count < n:
    temp = res[0]
    res[0] = res[1]
    res[1] = res[1] + temp
    count += 1

print(*res)