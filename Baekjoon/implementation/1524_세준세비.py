for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    li1 = sorted(list(map(int, input().split())), reverse=True)
    li2 = sorted(list(map(int, input().split())), reverse=True)
    while li1 and li2:
        if li1[-1] >= li2[-1]:
            li2.pop()
        else:
            li1.pop()
    if li1:
        print('S')
    elif li2:
        print('B')
    else:
        print('C')