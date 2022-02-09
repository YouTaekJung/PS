n = start = int(input())
count = 0
while True:

    num = n // 10 + n % 10
    count += 1
    n = int(str(n % 10) + str(num % 10))
    if (start == n):
        break
print(count)