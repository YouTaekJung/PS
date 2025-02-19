const count = num => {
    let count = 0
    while (num !== 1) {
        num % 2 ? num = (num - 1) / 2 : num = num / 2
        count += 1
    }
    return count
}

function solution(num_list) {
    return num_list.reduce((acc, cur) => acc + count(cur),0)
}