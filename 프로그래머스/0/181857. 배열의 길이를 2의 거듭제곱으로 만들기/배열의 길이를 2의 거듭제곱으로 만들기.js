function solution(arr) {
    let n = arr.length
    let target = 1

    while (target < n) {
        target *= 2
    }

    while (arr.length < target) {
        arr.push(0)
    }

    return arr
}