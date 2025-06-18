function solution(n) {
    let res = 1, acc = 1
    while (res <= 10) {
        acc *= res
        if (acc > n) return res - 1
        res += 1
    }
    return 10
}