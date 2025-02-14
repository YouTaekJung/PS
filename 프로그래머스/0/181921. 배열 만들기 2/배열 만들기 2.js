function solution(l, r) {
    const result = []

    for (let i = l; i <= r; i++) {
        if (/^[05]+$/.test(i)) result.push(i)
    }

    return result.length ? result : [-1]
}
