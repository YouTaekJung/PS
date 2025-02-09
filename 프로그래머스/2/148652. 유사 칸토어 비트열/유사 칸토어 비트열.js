const recur = (num) => {
    if (num % 5 === 2) return 0
    if (num < 5) return 1
    return recur(parseInt(num / 5))
}

const solution = (n, l, r) => {
    let res = 0
    for (let i = l - 1; i < r; i++) {
        res += recur(i)

    }
    return res
}