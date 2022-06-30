n = int(input())
for _ in range(n):
    a, b = input().split()
    la, lb = sorted(a), sorted(b)
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
        continue
    for ca, cb in zip(la, lb):
        if ca != cb:
            print(f'{a} & {b} are NOT anagrams.')
            break
    else:
        print(f'{a} & {b} are anagrams.')