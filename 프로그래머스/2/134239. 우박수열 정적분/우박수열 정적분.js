const solution = (k, ranges) => {
    const dp = [0], res = []
    while (k > 1) {
        let next = k
        next = k % 2 ? 3 * next + 1 : k / 2
        dp.push((dp.at(-1) ?? 0) + (k + next) / 2)
        k = next
    }

    const len = dp.length - 1
    for (let range of ranges) {
        let [start, end] = range
        res.push(len + end < start ? -1 : dp[len + end] - dp[start])
    }
    return res
}