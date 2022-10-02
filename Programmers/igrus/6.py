n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for b in board:
    print(sum(b))