from collections import deque

n, m = map(int, input().split())
board = []
red, blue = [], []
q = deque()
for i in range(n):
    li = list(input())
    for j, l in enumerate(li):
        if l == 'R':
            red = [i, j]
        elif l == 'B':
            blue = [i, j]
    board.append(li)

print(red, blue)
ans = 0




print(-1)