vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input().lower()
    if word == '#':
        break
    print(sum(map(lambda x: word.count(x), vowel)))