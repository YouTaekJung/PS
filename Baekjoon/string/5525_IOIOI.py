n, m = int(input()), int(input())
word = input()
ans, i, count = 0, 0, 0

while i < (m - 1):
    if word[i:i + 3] == 'IOI':
        i += 2
        count += 1
        if count >= n:
            ans += 1
    else:
        i += 1
        count = 0

print(ans)