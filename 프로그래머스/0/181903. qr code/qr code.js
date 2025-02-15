function solution(q, r, code) {
    let res = ''
    for (let i = 0; i < code.length; i++) {
        if (i % q === r) res += code[i]
    }
    return res
}