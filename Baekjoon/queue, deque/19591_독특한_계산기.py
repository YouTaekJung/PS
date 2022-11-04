from collections import deque

def pop_append_left(val):
    op.popleft()
    num.popleft()
    num.popleft()
    num.appendleft(val)

def pop_append_right(val):
    op.pop()
    num.pop()
    num.pop()
    num.append(val)

s = input()
op, num, temp = deque([]), deque([]), ''

for i, c in enumerate(s):
    if i != 0 and c in ['*', '/', '+', '-']:
        op.append(c)
        num.append(str(int(temp)))
        temp = ''
    else:
        temp += c
num.append(str(int(temp)))


while op:
    left = str(int(eval(num[0] + op[0] + num[1])))
    right = str(int(eval(num[-2] + op[-1] + num[-1])))
    if op[0] in ['*', '/'] and op[-1] in ['*', '/']:
        if int(left) >= int(right):
            pop_append_left(left)
        else:
            pop_append_right(right)
    elif op[0] in ['*', '/']:
        pop_append_left(left)
    elif op[-1] in ['*', '/']:
        pop_append_right(right)
    else:
        if int(left) >= int(right):
            pop_append_left(left)
        else:
            pop_append_right(right)
print(int(num[0]))