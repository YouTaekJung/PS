function solution(arr) {
    const [left, right] = [arr.indexOf(2), arr.lastIndexOf(2)]
    return left >= 0 ? arr.slice(left, right + 1): [-1]
}