const solution = (n) => {
    const res = []
    while (n > 1) {
        res.push(n)
        if (n % 2) {
            n = 3 * n + 1
        } else {
            n = n / 2
        }
    }
    return [...res, 1]
}