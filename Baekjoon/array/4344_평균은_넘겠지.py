n = int(input())

for _ in range(n):
    li = list(map(int, input().split()))
    ave = sum(li[1:]) / li[0]
    c = 0
    for score in li[1:]:
        if score > ave:
            c += 1
    res = c / li[0] * 100
    print(f'{res:.3f}%')