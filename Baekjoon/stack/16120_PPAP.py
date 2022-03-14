li = list(input())
stack = []

for i in range(len(li)):
    if li[i] == 'P' and stack[-3:] == ['P', 'P', 'A']:
        for _ in range(2):
            stack.pop()
    else:
        stack.append(li[i])

if stack == ['P']:
    print('PPAP')
else:
    print('NP')