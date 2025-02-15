function solution(arr, queries) {
    for (let query of queries) {
        const [s, e, k] = query
        for (let i = s; i <= e; i++) {
            if (!(i % k)) arr[i] += 1
        }
    }
    return arr
}