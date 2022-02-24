e, s, m = map(int, input().split())

i = 1
e = 0 if e == 15 else e
m = 0 if m == 19 else m
s = 0 if s == 28 else s

while True:
    if i % 15 == e and i % 28 == s and i % 19 == m:
        print(i)
        break
    i += 1