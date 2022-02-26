import sys
n = int(sys.stdin.readline())

d = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        d.insert(0, command[1])
    elif command[0] == 'push_back':
        d.append(command[1])
    elif command[0] == 'pop_front':
        print(-1 if len(d) == 0 else d.pop(0))
    elif command[0] == 'pop_back':
        print(-1 if len(d) == 0 else d.pop(-1))
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        print(1 if len(d) == 0 else 0)
    elif command[0] == 'front':
        print(-1 if len(d) == 0 else d[0])
    elif command[0] == 'back':
        print(-1 if len(d) == 0 else d[-1])