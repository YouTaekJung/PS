import sys
n = int(sys.stdin.readline())

s = [0] * 21
for i in range(n):
    command = sys.stdin.readline().split()

    if len(command) > 1:
        command[1] = int(command[1])
    if command[0] == 'add':
        s[command[1]] = 1
    elif command[0] == 'remove':
        s[command[1]] = 0
    elif command[0] == 'check':
        print(s[command[1]])
    elif command[0] == 'toggle':
        s[command[1]] = abs(s[command[1]] - 1)
    elif command[0] == 'all':
        s = [0] + [1] * 20
    elif command[0] == 'empty':
        s = [0] * 21