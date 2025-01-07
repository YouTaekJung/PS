function solution(order) {
    const stack = [], li = Array(order.length).fill(0).map((_, idx) => idx + 1)
    let res = 0
    
    for (let i = 1; i <= order.length; i++) {
        stack.push(i);
        while (stack.length !== 0 && stack.at(-1) === order[res]) {
            stack.pop();
            res += 1
        }
    }
    return res;
}