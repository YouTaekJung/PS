function solution(my_string, m, c) {
    let res = ''
    for (let i = 0; i < my_string.length; i++) {
        if (i % m === c - 1) res += my_string[i]
    }
    return res
}