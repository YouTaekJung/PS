function solution(code) {
    let mode = 0, ret = ''
    for (let i = 0; i < code.length; i++) {
        if (mode) {
            code[i] === '1' ? (mode = 0) : (i % 2 !== 0 && (ret += code[i]))
        } else {
            code[i] === '1' ? (mode = 1) : (i % 2 === 0 && (ret += code[i]))   
        }
    }
    return ret.length > 0 ? ret : "EMPTY";
}