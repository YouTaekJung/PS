for i in range(1, 4):
    globals()[f'x{i}'], globals()[f'y{i}'] = map(int, input().split())

ccw = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
if ccw == 0:
    print(0)
else:
    print(abs(ccw) // ccw)