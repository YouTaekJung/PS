while True:
    li = list(map(int, input().split()))
    if li == [0, 0, 0]:
        break
    sum = 0
    m = max(li)
    for i in range(3):
        if li[i] == m:
            sum += li[i] ** 2
        else:
            sum -= li[i] ** 2
    print("right" if sum == 0 else "wrong")

