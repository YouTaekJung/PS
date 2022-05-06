n = int(input())
for _ in range(n):
    word = input().split()
    print(' '.join(word[2:]) + ' ' + ' '.join(word[:2]))