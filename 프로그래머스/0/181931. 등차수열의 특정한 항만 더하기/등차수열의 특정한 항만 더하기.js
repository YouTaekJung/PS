function solution(a, d, included) {
    return included.reduce((acc, cur, i) => {
        return cur ? acc + a + i * d : acc
    }, 0)
}