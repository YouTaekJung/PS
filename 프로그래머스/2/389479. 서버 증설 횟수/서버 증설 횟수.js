function solution(players, m, k) {
    let res = 0
    const computer = []
    for (let i = 0; i < players.length; i++) {
        while (computer[0] === i) computer.shift()
        if (Math.floor(players[i] / m) > computer.length) {
            let count = Math.floor(players[i] / m) - computer.length
            res += count
            while (count--) computer.push(i + k)
        }
    }
    return res
}