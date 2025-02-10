const getLargestProperDivisor = (n) => {
    if (n === 1) return 0
    let prime = 0
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            if (n / i > 1e7) {
                prime = i
                continue
            } else {
                return n / i
            }
        }
    }
    return prime || 1
}

function solution(begin, end) {
    return Array(end - begin + 1).fill(begin).map((num, idx) => getLargestProperDivisor(num + idx))
}
