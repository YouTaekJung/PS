n = int(input())
six = [1]

i = 2
while i * (2 * i - 1) <= n:
    six.append(i * (2 * i - 1))
    i += 1
print(six)