function solution(myString, pat) {
    return [...myString].reduce((acc, cur, idx) => {
        if(myString.slice(idx, pat.length + idx) === pat) return acc + 1
        return acc
    }, 0)
}