import sys
input = sys.stdin.readline
s1, s2 = list(input().strip()), []
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'P':
        s1.append(command[1])
    elif command[0] == 'L' and s1 != []:
        s2.append(s1.pop())
    elif command[0] == 'D' and s2 != []:
        s1.append(s2.pop())
    elif command[0] == 'B' and s1 != []:
        s1.pop()

print(''.join(s1 + s2[::-1]))
