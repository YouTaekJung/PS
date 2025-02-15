function solution(my_string, indices) {
    let res = ''
    indices.sort((a, b) => a - b)
    for (let i = 0; i < my_string.length; i++) {
        if (indices[0] === i) indices.shift()
        else res += my_string[i]
    }
    return res
}
