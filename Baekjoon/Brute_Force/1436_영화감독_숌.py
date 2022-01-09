n = int(input())

count = 0
num = 666
while count < n:
    if str(num).find("666") >= 0:
        count += 1
    num += 1

print(num - 1)