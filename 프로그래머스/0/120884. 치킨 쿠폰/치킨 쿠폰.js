function solution(chicken) {
    let res = 0
    while (chicken >= 10) {
        chicken -= 9
        res++
    }
    return res
}