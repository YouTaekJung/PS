key = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
p, w = map(int, input().split())
text = input()

ans = 0
prev = ''
for i in range(len(text)):
    if text[i] == ' ':
        ans += p
        prev = ''
    for j in range(len(key)):
        for k in range(len(key[j])):
            if text[i] == key[j][k]:
                if j == prev:
                    ans += w
                ans += (1 + k) * p
                prev = j
print(ans)

