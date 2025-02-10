const combinations = (arr, k) => {
    const result = []
    const combine = (start, combo) => {
        if (combo.length === k) {
            result.push([...combo])
            return
        }
        for (let i = start; i < arr.length; i++) {
            combo.push(arr[i])
            combine(i + 1, combo)
            combo.pop()
        }
    }

    combine(0, [])
    return result
}

const solution = (n, q, ans) => {
    let com = combinations(Array(n).fill(1).map((num, i) => num + i), 5)
    let res = 0
    for (let c of com) {
        for (let i = 0; i < q.length; i++) {
            if (c.filter(num => q[i].includes(num)).length !== ans[i]) break
            if (i === q.length - 1) res += 1
        }
    }
    return res
}