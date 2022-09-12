def cal(num, weight):
    if num > n:
        return

    if d[num][weight]:
        return
    d[num][weight] = 1

    cal(num + 1, weight + li[num - 1])
    cal(num + 1, abs(weight - li[num - 1]))
    cal(num + 1, weight)


n = int(input())
li = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
d = [[0] * 15001 for _ in range(31)]

cal(0, 0)

for t in target:
    if t > 15000:
        print("N", end=" ")
    elif d[n][t]:
        print("Y", end=" ")
    else:
        print("N", end=" ")