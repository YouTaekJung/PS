word = list(input())

check = 1
i = 0
while i < len(word):
    if word[i] == '<':
        i += 1
        while word[i] != '>':
            i += 1
        i += 1
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        temp = word[start:i][::-1]
        word[start:i] = temp
    else:
        i += 1

print(''.join(word))
