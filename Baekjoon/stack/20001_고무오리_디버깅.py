stack = []

while True:
    s = input()
    if s == '문제':
        stack.append(1)
    elif s == '고무오리':
        if not stack:
            stack += [1, 1]
        else:
            stack.pop()
    elif s == '고무오리 디버깅 끝':
        break

print('힝구' if stack else '고무오리야 사랑해')