import sys
n = int(sys.stdin.readline())

queue = []
cur = 0
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) > cur:
            print(queue[cur])
            cur += 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue) - cur if len(queue) > cur else 0)
    elif command[0] == 'empty':
        print(0 if len(queue) > cur else 1)
    elif command[0] == 'front':
        print(queue[cur] if len(queue) > cur else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue) > cur else -1)