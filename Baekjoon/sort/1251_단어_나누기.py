li = list(input())
answer, temp = [], []

for i in range(1, len(li) - 1):
    for j in range(i + 1, len(li)):
        a = li[:i][::-1]
        b = li[i:j][::-1]
        c = li[j:][::-1]
        temp.append(a + b + c)

for t in temp:
    answer.append(''.join(t))

print(sorted(answer)[0])