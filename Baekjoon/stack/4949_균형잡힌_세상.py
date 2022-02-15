while True:
    word = input()
    if word == '.':
        break
    stack = []
    for i in range(len(word)):
        if word[i] == '(':
            stack.append("(")
        elif word[i] == ')':
            if len(stack) == 0:
                print("no")
                break
            if stack.pop() != "(":
                print("no")
                break
        elif word[i] == '[':
            stack.append("[")
        elif word[i] == ']':
            if len(stack) == 0:
                print("no")
                break
            if stack.pop() != "[":
                print("no")
                break
        if word[i] == '.':
            print("yes" if len(stack) == 0 else "no")