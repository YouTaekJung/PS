function solution(sequence, k) {
    let [left, right, acc] = [0, 0, sequence[0]]
    const res = []
    while (right < sequence.length && left <= right) {
        if (acc < k) {
            right += 1
            acc += sequence[right]
        } else {
            if (acc === k) res.push([right - left, left, right])
            acc -= sequence[left]
            left += 1
        }
            
    }
    return res.sort((a, b) => a[0] - b[0] || a[1] - b[1])[0].slice(1)
}