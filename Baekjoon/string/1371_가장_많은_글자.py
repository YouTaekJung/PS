check = [0] * 26
while True:
    try:
        s = input()
        for c in s:
            if c != ' ':
                check[ord(c) - 97] += 1
    except:
        break
m = max(check)
for i, c in enumerate(check):
    if c == m:
        print(chr(i + 97), end='')