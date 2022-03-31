n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]

def divide(b):
    if len(b) == 1:
        return str(b[0][0])

    check = b[0][0]
    for i in range(len(b)):
        for j in range(len(b)):
            if check != b[i][j]:
                h = len(b) // 2
                return ('(' + divide(list(map(lambda x: x[:h], b[:h]))) +
                        divide(list(map(lambda x: x[h:], b[:h]))) +
                        divide(list(map(lambda x: x[:h], b[h:]))) +
                        divide(list(map(lambda x: x[h:], b[h:]))) + ')')
    return str(b[0][0])

print(divide(board))
