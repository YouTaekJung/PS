t = int(input())

for _ in range(t):
    check= [0] * 27
    s = input()
    for i in range(len(s)):
        check[int(ord(s[i])) - 65] += 1

    ans = 0
    for i in range(26):
        if check[i] == 0:
            ans += i + 65

    print(ans)