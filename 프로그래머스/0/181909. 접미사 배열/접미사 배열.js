function solution(my_string) {
    let res = [], s = ''
    for (let i = my_string.length - 1; i >= 0; i--) {
        s = my_string[i] + s
        res.push(s)
    }
    return res.sort()
}