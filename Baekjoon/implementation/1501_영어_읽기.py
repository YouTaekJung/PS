from functools import reduce
d = {}

def sort_word(word):
    if len(word) == 1:
        return word
    return word[0] + word[-1] + ''.join(sorted(word[1:-1]))

n = int(input())
for _ in range(n):
    word = sort_word(input())
    d[word] = d.get(word, 0) + 1

for _ in range(int(input())):
    sentence = input().split()
    li = []
    for s in sentence:
        word = sort_word(s)
        li.append(d[word] if word in d else 0)
    print(reduce(lambda acc, cur: acc * cur, li, 1))