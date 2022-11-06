num = input()
for i in range(len(num) - 1):
    left, right = 1, 1
    for j in range(i + 1):
        left *= int(num[j])
    for k in range(i + 1, len(num)):
        right *= int(num[k])
    if left == right:
        print('YES')
        exit()
print('NO')