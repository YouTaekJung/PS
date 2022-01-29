i = 0
li = []
while i < 10:
    li.append(int(input()) % 42)
    i += 1
print(len(set(li)))