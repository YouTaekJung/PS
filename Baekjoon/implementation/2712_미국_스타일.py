for _ in range(int(input())):
    a, b = input().split()
    if b == 'kg':
        print('%.4f %s' % (float(a)*2.2046, 'lb'))
    elif b == 'lb':
        print('%.4f %s' % (float(a)*0.4536, 'kg'))
    elif b == 'l':
        print('%.4f %s' % (float(a)*0.2642, 'g'))
    elif b == 'g':
        print('%.4f %s' % (float(a)*3.7854, 'l'))