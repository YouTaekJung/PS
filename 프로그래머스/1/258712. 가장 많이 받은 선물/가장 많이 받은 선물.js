function solution(friends, gifts) {
    const record = friends.reduce((obj, cur) => {
        obj[cur] = friends.reduce((count, name) => {
            if (cur !== name) count[name] = 0
            return count
        }, {})
        return obj
    }, {})
    const index = friends.reduce((obj, cur) => {
        obj[cur] = 0
        return obj
    }, {})

    gifts.forEach(gift => {
        const [give, take] = gift.split(' ')
        record[give][take] = (record[give][take] || 0) + 1
        record[take][give] = (record[take][give] || 0) - 1
        index[give] += 1
        index[take] -= 1
    })

    const res = friends.slice().map(friend => {
        let gift = 0
        Object.entries(record[friend]).forEach(([name, count]) => {
            if (count > 0) gift += 1
            else if (count === 0) {
                if (index[friend] > index[name]) gift += 1
            }
        })
        return gift
    })
    return Math.max(...res) 
}