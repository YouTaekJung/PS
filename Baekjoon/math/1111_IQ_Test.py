n = int(input())
li = list(map(int, input().split()))

if len(li) == 1:
    print('A')
elif len(set(li)) == 1:
    print(li[0])
elif len(li) == 2:
    print('A')
else:
    a = (li[1] - li[2]) // (li[0] - li[1]) if (li[0] - li[1]) else 0
    b = li[1] - li[0] * a
    for i in range(n - 1):
        if (li[i + 1] != li[i] * a + b):
            print('B')
            exit()
    print(li[-1] * a + b)