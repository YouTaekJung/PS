function solution(board) {
    const dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    const dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    let res = 0
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            let check = true
            for (let k = 0; k < 9; k++) {
                const [nx, ny] = [i + dx[k], j + dy[k]]
                if (nx < 0 || ny < 0 || nx >= board.length || ny >= board[0].length) continue
                if (board[nx][ny] === 1) {
                    check = false
                    break
                }
            }
            if (check) res++
        }
    }
    return res
}