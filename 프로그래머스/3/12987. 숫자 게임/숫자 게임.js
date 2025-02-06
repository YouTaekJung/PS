function solution(A, B) {
    A = A.sort((a, b) => b - a)
    B = B.sort((a, b) => b - a)
    let res = 0, Ai = 0, Bi =0, Bj = A.length - 1
    while (Bi <= Bj) {
        if (A[Ai] < B[Bi]) {
            res += 1
            Bi += 1
        } else {
            Bj -= 1
        }
        Ai += 1
    }
    return res
}