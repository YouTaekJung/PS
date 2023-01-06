n = int(input())

while True:
    cur = int(input())
    if cur == 0:
        break
    elif cur % n == 0:
        print("%s is a multiple of %s." % (cur, n))
    else:
        print("%s is NOT a multiple of %s." % (cur, n))