word = input()
stack, ans = [], ''

for w in word:
    if w.isalpha():
        ans += w
    else:
        if w == '(':
            stack.append(w)
        elif w == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif w in ['+', '-']:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(w)
        else:
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(w)

while stack:
    ans += stack.pop()

print(ans)