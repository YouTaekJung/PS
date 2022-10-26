def merge_sort(li, left, right):
    if left < right and count <= k:
        mid = (left + right) // 2
        merge_sort(li, left, mid);
        merge_sort(li, mid + 1, right);
        merge(li, left, mid, right);

def merge(li, left, mid, right):
    global count, ans
    i, j = left, mid + 1
    temp = []
    while i <= mid and j <= right:
        if li[i] <= li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1

    while i <= mid:
        temp.append(li[i])
        i += 1
    while j <= right:
        temp.append(li[j])
        j += 1

    j = 0
    for i in range(left, right + 1):
        li[i] = temp[j]
        count += 1
        if count == k:
            ans = li[i]
            break;
        j += 1

n, k = map(int, input().split())
li = list(map(int, input().split()))
count, ans = 0, -1
merge_sort(li, 0, n - 1)
print(ans)