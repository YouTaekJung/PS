function solution(n, control) {
    return control.split('').reduce((acc, cur) => {
        if (cur === 'w') return acc + 1
        if (cur === 's') return acc - 1
        if (cur === 'd') return acc + 10
        if (cur === 'a') return acc - 10
    }, n)
}