t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    li_a, li_b = [], []
    while a >= 1:
        li_a.append(a)
        a //= 2
    while b >= 1:
        li_b.append(b)
        b //= 2
    for i in range(len(li_a)):
        if li_a[i] in li_b:
            print(10 * li_a[i])
            break
