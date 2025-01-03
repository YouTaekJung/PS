function solution(ingredient) {
    let result = 0
    const stack = []
    ingredient.forEach(i => {
        stack.push(i)
        if (stack.at(-4) === 1 && stack.at(-3) === 2 && stack.at(-2) === 3 && stack.at(-1) === 1) {
            stack.splice(-4)
            result += 1
        }
    })
    return result
}