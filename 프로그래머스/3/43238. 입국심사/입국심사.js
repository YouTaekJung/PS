function solution(n, times) {
    let [left, right] = [1, Math.max(...times) * n]
    let res = right

    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        const people = times.reduce((sum, time) => sum + Math.floor(mid / time), 0)

        if (people >= n) {
            res = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return res
}
