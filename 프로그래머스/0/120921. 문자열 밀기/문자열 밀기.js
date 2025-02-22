function solution(A, B) {
    let res = 0
    while (A !== B && res < A.length) {
        A = A[A.length - 1] + A.slice(0, A.length - 1)
        res += 1
    }
    return res === A.length ? -1 : res
}