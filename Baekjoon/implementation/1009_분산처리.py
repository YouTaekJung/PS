n = int(input())

for _ in range(n):
    num, count = map(int, input().split())
    li = []
    acc = 1
    while True:
        acc = (acc * num) % 10
        if acc not in li:
            li.append(acc)
        else:
            break
    res = li[(count % len(li)) - 1]
    print(10 if res == 0 else res)