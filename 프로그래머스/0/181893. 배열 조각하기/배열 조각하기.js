function solution(arr, query) {
    for(let i = 0; i < query.length; i++) {
        const cur = query[i]
        if(i % 2) arr.splice(0, cur)
        else arr.splice(cur + 1, arr.length - cur - 1)
    }
    return arr
}