function solution(n) {
    let ans = [1], i = 2
    while (i <= n) {
        if (!(n % i)) ans.push(i)
        i++
    }
    return ans
}