function solution(X, Y) {
    const count = Array.from(Array(10), () => Array(2).fill(0))
    for (let i = 0; i < X.length; i++) {
        count[X[i]][0] += 1
    }
    for (let i = 0; i < Y.length; i++) {
        count[Y[i]][1] += 1
    }
    let res = ''
    for (let i = 0; i < 10; i++) {
        res = String(i).repeat(Math.min(count[i][0],count[i][1])) + res
    }
    if (new Set(res).size === 1 && res[0] === '0') return '0'
    return res === '' ? '-1' : res
}