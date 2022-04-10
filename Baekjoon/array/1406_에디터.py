import sys
input = sys.stdin.readline
s = list(input().rstrip())
n = int(input())


cursor = len(s)
for i in range(n):
    command = input().split()
    if command[0] == 'L':
        cursor = max(cursor - 1, 0)
    elif command[0] == 'D':
        cursor = min(len(s), cursor + 1)
    elif command[0] == 'B':
        if cursor != 0:
            s.remove(s[cursor - 1])
            cursor -= 1
    else:
        s.insert(cursor, command[1])
        cursor += 1
print(''.join(s))


