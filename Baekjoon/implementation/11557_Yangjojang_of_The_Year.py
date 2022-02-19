n = int(input())
for _ in range(n):
    m = int(input())
    cur_max = 0
    res_name = ''
    for _ in range(m):
        name, count = input().split()
        if cur_max < int(count):
            cur_max = int(count)
            res_name = name
    print(res_name)