li = list(input())
stack = []

for i in range(len(li)):
    if li[i] == ')':
        count = 0
        while True:
            cur = stack.pop()
            if cur == '(':
                break
            count += cur
        stack.append(int(stack.pop()) * count)
    elif li[i] == '(':
        stack.append('(')
    elif i != len(li) - 1 and li[i].isdigit() and li[i + 1] == '(':
        stack.append(int(li[i]))
    else:
        stack.append(1)
print(sum(stack))