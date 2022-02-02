n = int(input())

for _ in range(n):
    m, s = input().split()
    str = ''
    for i in range(len(s)):
        str += s[i] * int(m)

    print(str)