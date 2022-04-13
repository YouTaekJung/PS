n = int(input())
word = input()
ans = ''

for i, w in enumerate(word):
    if i % n == 0:
        ans += w

print(ans)