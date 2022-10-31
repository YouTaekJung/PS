def java_to_cpp(s):
    ans = ''
    i = 0
    while i < len(s):
        if s[i].isupper():
            ans += '_' + s[i].lower()
        else:
            ans += s[i]
        i += 1
    return ans

def cpp_to_java(s):
    ans = ''
    i = 0
    while i < len(s):
        if s[i] == '_':
            ans += s[i + 1].upper()
            i += 1
        else:
            ans += s[i]
        i += 1
    return ans

def is_cpp(s):
    if '_' in [s[0], s[-1]] or s[0].isupper():
        return False
    for i, c in enumerate(s):
        if ord(c) == 95:
            if 97 > ord(s[i + 1]) or ord(s[i + 1]) > 122:
                return False
            continue
        if 97 <= ord(c) <= 122:
            continue
        return False
    return True

def is_java(s):
    if s[0].isupper():
        return False
    for c in s:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            continue
        return False
    return True

s = input()
if is_cpp(s):
    print(cpp_to_java(s))
elif is_java(s):
    print(java_to_cpp(s))
else:
    print('Error!')