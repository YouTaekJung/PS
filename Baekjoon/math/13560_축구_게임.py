n = int(input())
li = sorted(list(map(int, input().split())))

def check():
    s = 0
    if sum(li) != n * (n - 1) // 2:
        return -1
    for i, l in enumerate(li[:-1]):
        s += l
        if s < i * (i + 1) // 2:
            return -1
    return 1

print(check())