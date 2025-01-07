const solution = (want, number, discount) => {
    const hash = Array(want.length).fill(0).map((_, index) => index)
                    .reduce((acc, cur) => {
                        acc[want[cur]] = number[cur]
                        return acc
                    }, {})

    for (let i = 0; i < 10; i++) {
        if (discount[i] in hash) hash[discount[i]] -= 1
    }
    
    let [left, right, res] = [0, 10, 0]
    if (Object.values(hash).every(count => count === 0)) res += 1
    
    while (right < discount.length) {
        const [dLeft, dRight] = [discount[left], discount[right]]
        if (dLeft in hash) hash[dLeft] += 1
        if (dRight in hash) hash[dRight] -= 1
        if (Object.values(hash).every(count => count === 0)) res += 1
        left += 1
        right += 1
    }

    return res
}
