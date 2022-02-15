word = input()
rem = list(input())
l = len(rem)
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == rem[-1] and stack[-l:] == rem:
        for _ in range(l):
            stack.pop()

print(''.join(stack) if len(stack) else 'FRULA')