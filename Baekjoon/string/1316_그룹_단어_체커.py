n = int(input())
res = 0

for _ in range(n):
    word = input()
    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i]==word[i+1]:
                pass
            elif word[i] in word[i + 1:]:
                break
        else:
            res += 1
print(res)