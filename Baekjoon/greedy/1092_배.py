n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if box[0] > crane[0]:
    print(-1)
    exit()
ans = 0
while box:
    if not box:
        break
    for c in crane:
        for b in box:
            if c >= b:
                box.remove(b)
                break
    ans += 1
print(ans)