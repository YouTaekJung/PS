function solution(n) {
    let i = 2
    const ans = new Set()
    while (i <= n) {
        if (n % i === 0) {
            n /= i
            ans.add(i)
        } else {
            i++
        }
    }
    return [...ans]
}