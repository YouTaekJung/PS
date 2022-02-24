while True:
    try:
        n = int(input())
        i = 1
        while True:
            if i % n == 0:
                print(len(str(i)))
                break
            i = 10 * i + 1
    except:
        break