li = input().split('-')

for i in range(len(li)):
    li[i] = -sum(list(map(int, li[i].split('+'))))

li[0] *= -1
print(sum(li))