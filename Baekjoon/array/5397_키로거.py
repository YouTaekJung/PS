for _ in range(int(input())):
    left, right = [], []
    s = input()

    for x in s:
        if x == '>':
            if right:
                left.append(right.pop())
        elif x == '<':
            if left:
                right.append(left.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)
    print(''.join(left) + ''.join(right[::-1]))