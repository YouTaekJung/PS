const solution = (diffs, times, limit) => {
    let [left, right] = [1, diffs.reduce((acc, cur) => Math.max(acc, cur), 1)]
    while (left < right) {
        const check = parseInt((left + right) / 2)
        let cur = 0
        for (let i = 0; i < diffs.length; i++) {
            if (check >= diffs[i]) cur += times[i]
            else cur += (diffs[i] - check) * (times[i] + times[i - 1]) + times[i] 
        }
        if (cur > limit) left = check + 1
        else right = check
    }
    return left
}