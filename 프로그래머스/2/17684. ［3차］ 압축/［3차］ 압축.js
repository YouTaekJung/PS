const solution = (msg) => {
    const obj = Array(26).fill(0).map((el, idx) => idx + 1)
    .reduce((acc, cur) => {
        acc[String.fromCharCode(cur + 64)] = cur
        return acc
    }, {})
    
    const res = []
    let num = 27, i = 0, cur
    while (i < msg.length) {
        cur = msg[i]
        while (cur in obj) {
            i += 1
            if (i === msg.length) break
            cur += msg[i]
        }
        if (i === msg.length) break
        res.push(obj[cur.slice(0, -1)])
        obj[cur] = num
        num += 1
    }
    return [...res, obj[cur]]
}