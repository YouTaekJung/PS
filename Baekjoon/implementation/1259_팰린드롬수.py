while True:
    s = input()
    if s == '0':
        break
    print('yes' if int(s) == int(s[::-1]) else 'no')