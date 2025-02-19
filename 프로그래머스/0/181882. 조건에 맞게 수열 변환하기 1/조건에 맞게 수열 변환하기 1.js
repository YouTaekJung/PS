function solution(arr) {
    return arr.map(el => {
        if (el >= 50) return el % 2 ? el : el / 2
        return el % 2 ? el * 2 : el
    })
}