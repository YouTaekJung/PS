n = int(input())
li = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        n = a % b
        a, b = b, n
    return a

for i in range(1, n):
    g = gcd(li[0], li[i])
    print(f'{li[0]//g}/{li[i]//g}')