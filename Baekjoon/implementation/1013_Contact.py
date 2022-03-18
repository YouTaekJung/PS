import re
t = int(input())
p = re.compile('(100+1+|01)+')

for _ in range(t):
    n = input()
    print('YES' if p.fullmatch(n) else 'NO')