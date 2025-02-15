function solution(arr, queries) {
    const res = []
    for (let query of queries) {
        const [s, e, k] = query
        let cur = 1e6 + 1
        for (let i = s; i <= e; i++) {
            if (arr[i] > k) cur = Math.min(cur, arr[i])
        }
        res.push(cur === 1e6 + 1 ? -1 : cur)
    }
    return res
}