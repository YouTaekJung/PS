x = list(input())
y = list(input())

count = 0
for w in x:
    if w in y:
        y.remove(w)
        count += 1
print(len(x) + len(y) - count)