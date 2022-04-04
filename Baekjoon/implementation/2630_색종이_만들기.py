n = int(input())
board = [input().split() for _ in range(n)]
ans = [0, 0]
def divide(b):
    global ans
    check = b[0][0]
    if len(b) == 1:
        if check == '1':
            ans[1] += 1
        else:
            ans[0] += 1
        return str(b[0][0])

    for i in range(len(b)):
        for j in range(len(b)):
            if check != b[i][j]:
                h = len(b) // 2
                divide(list(map(lambda x: x[:h], b[:h])))
                divide(list(map(lambda x: x[h:], b[:h])))
                divide(list(map(lambda x: x[:h], b[h:])))
                divide(list(map(lambda x: x[h:], b[h:])))
                return
    if check == '1':
        ans[1] += 1
    else:
        ans[0] += 1
    return

divide(board)
for a in ans:
    print(a)