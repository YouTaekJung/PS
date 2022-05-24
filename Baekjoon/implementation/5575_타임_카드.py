for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    time = 3600 * (h2 - h1) + 60 * (m2 - m1) + (s2 - s1)
    print(time // 3600, time % 3600 // 60, time % 60)