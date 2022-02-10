n = int(input())

for _ in range(n):
    res = []
    li = input().split()
    for i in range(len(li)):
        temp = list(li[i])
        temp.reverse()
        res.append(''.join(temp))
    print(' '.join(res))