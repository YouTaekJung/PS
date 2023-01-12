n, l = list(map(int, input().split()))

num = 1
ans = 0
while True:
    if str(l) not in str(num):
        ans += 1
        if ans == n:
            print(num)
            break
        num += 1
    else:
        num += 1