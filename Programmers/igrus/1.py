n = int(input())

print('int a;')
print('int *ptr = &a;')
for i in range(2, n + 1):
    print(f'int {"*" * i}ptr{i} = &ptr{i - 1 if i > 2 else ""};')
