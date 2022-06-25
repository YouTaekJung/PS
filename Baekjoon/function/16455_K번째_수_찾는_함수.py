def kth(a, k):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left, mid, right = [], [], []
    for i in range(len(a)):
        if a[i] < pivot:
            left.append(a[i])
        elif a[i] > pivot:
            right.append(a[i])
        else:
            mid.append(a[i])
    if k < len(left):
        return kth(left, k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return kth(right, k - len(left) - len(mid))