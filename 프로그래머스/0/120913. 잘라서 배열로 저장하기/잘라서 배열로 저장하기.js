function solution(my_str, n) {
    const strArr = my_str.split('')
    const ans = []
    while (strArr.length > 0) {
        ans.push(strArr.splice(0, n).join(''))
    }
    
    return ans
}