function solution(arr, queries) {
    for (let query of queries) {
        const [x, y] = query
        const temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    }
    return arr
}