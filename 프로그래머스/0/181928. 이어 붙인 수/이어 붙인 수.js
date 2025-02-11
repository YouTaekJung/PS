function solution(num_list) {
    let odd = 0, even = 0
    for (let num of num_list) {
        if (num % 2) {
            odd = odd * 10 + num
        } else {
            even = even * 10 + num
        }
    }
    return odd + even
}