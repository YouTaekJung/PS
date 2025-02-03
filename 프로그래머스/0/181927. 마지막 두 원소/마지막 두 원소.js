function solution(num_list) {
    const [x, y] = num_list.slice(-2)
    return [...num_list, y > x ? y - x : 2 * y]
}