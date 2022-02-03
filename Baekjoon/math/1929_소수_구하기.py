m, n = map(int, input().split())

for num in range(m, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
        if i == num - 1:
            print(num)