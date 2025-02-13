const solution = (n, w, num) => {
    let res = 1
    const total = Math.ceil(n / w)
    const target = Math.ceil(num / w)
    const nRemain = n % w || n
    const numRemain = num % w || num
    if (total % 2 === target % 2 && nRemain < numRemain) res -= 1 
    if (total % 2 !== target % 2 && nRemain + numRemain <= w) res -= 1
    return total - target + res
}