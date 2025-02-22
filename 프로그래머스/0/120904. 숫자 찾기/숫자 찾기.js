function solution(num, k) {
    const idx = ('' + num).split('').indexOf('' + k)
    return idx === -1 ? -1 : idx + 1 
}