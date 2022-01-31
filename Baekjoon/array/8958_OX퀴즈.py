n = int(input())
for i in range(n):
    li = list(input())
    sum = 0
    c = 1
    for j in li:
        if j == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)