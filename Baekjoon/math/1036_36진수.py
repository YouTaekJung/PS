def itots(c):
    if '0' <= c <= '9':
        return int(c)
    return ord(c) - 55

def tstoi(c):
    if 0 <= c <= 9:
        return str(c)
    return chr(c + 55)

n = int(input())
check, s = [0] * 36, 0
for _ in range(n):
    word = input()
    for i, c in enumerate(word[::-1]):
        s += itots(c) * (36 ** i)
        check[itots(c)] += (35 - itots(c)) * (36 ** i)
k = int(input())
s += sum(sorted(check, reverse=True)[:k])
ans = ''
while s > 0:
    ans += tstoi(s % 36)
    s //= 36
print(ans[::-1] if ans != '' else '0')