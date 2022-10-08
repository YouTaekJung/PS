for i in range(int(input()), 3, -1):
    if all([s in ['4', '7'] for s in str(i)]):
        print(i)
        break