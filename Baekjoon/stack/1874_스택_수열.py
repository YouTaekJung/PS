n = int(input())
stack = []
res = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        res.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for r in res:
        print(r)