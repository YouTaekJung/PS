n = int(input())

for _ in range(n):
    word = input()
    count = 0
    for i in range(len(word)):
        if word[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                print("NO")
                break
        if i == len(word) - 1:
            print("YES" if count == 0 else "NO")