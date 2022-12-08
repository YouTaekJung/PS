li = [int(input()) for _ in range(7)]
li = sorted([l for l in li if l % 2])
if len(li):
    print(sum(li))
    print(li[0])
else:
    print(-1)