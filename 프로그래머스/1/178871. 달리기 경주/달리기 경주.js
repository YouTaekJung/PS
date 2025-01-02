function solution(players, callings) {
    const ranking = {}
    players.forEach((player, index) => ranking[player] = index)
    for (let curPlayer of callings) {
        const index = ranking[curPlayer]
        const prevPlayer = players[index - 1]
        players[index] = prevPlayer
        players[index - 1] = curPlayer 
        ranking[prevPlayer] += 1
        ranking[curPlayer] -= 1
    }
    return players
}