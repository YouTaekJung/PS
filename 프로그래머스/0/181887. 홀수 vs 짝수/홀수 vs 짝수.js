function solution(num_list) {
    return Math.max(
        num_list.reduce((acc, cur, idx) => idx % 2 ? acc + cur : acc, 0),
        num_list.reduce((acc, cur, idx) => idx % 2 ? acc : acc + cur, 0)
    )
}