i = 0
while True:
    i += 1
    try:
        cur = input()
        if '-' in cur:
            break

        stack, count = 0, 0
        for c in cur:
            if c == '{':
                stack += 1
            else:
                if stack >= 1:
                    stack -= 1
                else:
                    count += 1
                    stack += 1
        print(f'{i}. {count + stack // 2}')
    except:
        break