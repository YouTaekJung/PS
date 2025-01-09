function solution(targets) {
    targets.sort((a, b) => b[0] - a[0])

    let res = 1, check = targets[0][0]

    for (let i = 1; i < targets.length; i++) {
        const [start, end] = targets[i]
        if (end <= check) {
            check = start
            res++
        }
    }

    return res
}