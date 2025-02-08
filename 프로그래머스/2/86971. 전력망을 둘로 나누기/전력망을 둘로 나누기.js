const check = (hash, start, n) => {
    let count = 0
    const queue = [start]
    const visited = Array(n).fill(0)
    visited[start] = 1
    while (queue.length) {
        count += 1
        const cur = queue.shift()
        for (let num of hash[cur]) {
            if (!visited[num]) {
                queue.push(num)
                visited[num] = 1
            }
        }
    }
    return count
}

const solution = (n, wires) => {
    let res = 100
    for (let i = 0; i < wires.length; i++) {
        let [left, right] = wires[i]
        const hash = Array(n).fill(0).map((el, idx) => idx + 1).reduce((acc, cur) => {
                            acc[cur] = []
                            return acc
                        }, {})
        for (let j = 0; j < wires.length; j++) {
            if (i === j) continue
            const [x, y] = wires[j]
            hash[x].push(y)
            hash[y].push(x)
        }
        res = Math.min(res, Math.abs(check(hash, left, n) - check(hash, right, n)))
    }
    return res
}