function solution(storey) {
    let ans = 0

    while (storey > 0) {
        const digit = storey % 10
        const next = Math.floor(storey / 10)

        if (digit < 5) {
            ans += digit
            storey = next
        } else if (digit > 5) {
            ans += (10 - digit)
            storey = next + 1
        } else {
            if (next % 10 >= 5) {
                ans += 5
                storey = next + 1
            } else {
                ans += 5
                storey = next
            }
        }
    }

    return ans
}
