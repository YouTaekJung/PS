n = int(input())
count = 0
cur = 0

def check(num):
    for i in range(len(num) - 1):
        if num[i] <= num[i + 1]:
            return i + 1
    return -1

def bf(num, count):
    if count == n:
        return ''.join(num)
    last = idx = len(num) - 1
    while last == idx:
        for i in range(len(num) - 1):
            if num[i] <= num[i + 1]:
                idx = i
                break
        num[idx] += 1
    print(num)
    return bf(num, count)

if n <= 9:
    print(n)
else:
    print(bf([1, 0], 10))
