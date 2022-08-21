p, k = map(int, input().split())

for i in range(2, k):
    if not p % i:
        print('BAD', i)
        exit()

print('GOOD')
