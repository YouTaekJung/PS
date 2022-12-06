while True:
    n = int(input())
    if not n:
        break
    ans = 0
    for i in range(1, n + 1):
        if not (n ** 2) % i:
            s, d = ((n ** 2)/ i + i) / 2, ((n ** 2)/ i - i) / 2
            if int(s) == s and int(d) == d and d > n:
                ans += 1
    print(ans)