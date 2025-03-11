function solution(arr) {
    const res = []
    arr.forEach(el => res.push(...Array(el).fill(el)))
    return res
}