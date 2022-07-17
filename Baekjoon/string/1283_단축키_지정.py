n = int(input())
check = [0] * 26

for _ in range(n):
    s = input().split()
    i, ans = 0, False
    for i in range(len(s)):
        if not check[ord(s[i][0].lower()) - 97]:
            check[ord(s[i][0].lower()) - 97] = 1
            s[i] = '[' + s[i][0] + ']' + s[i][1:]
            ans = True
            break
    if ans:
        print(' '.join(s))
        continue

    s = ' '.join(s)
    for i, c in enumerate(s):
        if c != ' ' and not check[ord(c.lower()) - 97]:
            check[ord(c.lower()) - 97] = 1
            ans = True
            break
    print(f'{s[:i]}[{s[i]}]{s[i + 1:]}' if ans else s)