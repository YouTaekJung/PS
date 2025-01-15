const solution = (numbers) => {
    const stack = [[0, numbers[0]]], res = Array(numbers.length).fill(-1)
    for (let i = 1; i < numbers.length; i++) {
        while (stack.length && stack.at(-1)[1] < numbers[i]) {
            const [idx, cur] = stack.pop()
            res[idx] = numbers[i]
        }
        stack.push([i, numbers[i]])
    }
    return res
}