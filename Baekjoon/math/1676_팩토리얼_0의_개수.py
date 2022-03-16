n = int(input())
count = 0

for i in range(5, n + 1):
    while i != 0 and i % 5 == 0:
        i //= 5
        count += 1

print(count)