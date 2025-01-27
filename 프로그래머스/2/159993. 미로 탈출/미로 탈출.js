const bfs = (start, end, maps) => {
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    const visited = Array.from({ length: maps.length }, () => Array(maps[0].length).fill(0))
    visited[start[0]][start[1]] = 1
    const queue = [start]

    while (queue.length) {
        const [x, y, time] = queue.shift()
        for (let i = 0; i < 4; i++) {
            const [nx, ny] = [x + dx[i], y + dy[i]]
            if (0 <= nx && nx < maps.length
               && 0 <= ny && ny < maps[0].length
               && !visited[nx][ny]
                && maps[nx][ny] !== 'X'
               ) {
                    if (nx === end[0] && ny === end[1]) {
                        return time + 1
                    }
                    queue.push([nx, ny, time + 1])
                    visited[nx][ny] = 1
            }
        }
    }
    return -1
}

const solution = (maps) => {
    let s, l, e
    for (let i = 0; i < maps.length; i++) {
        for (let j = 0; j < maps[0].length; j++) {
            if (maps[i][j] === 'S') s = [i, j, 0]
            else if (maps[i][j] === 'L') l = [i, j, 0]
            else if (maps[i][j] === 'E') e = [i, j]
        }
    }
    const sTol = bfs(s, l, maps)
    const lToe = bfs(l, e, maps)
    if (sTol === -1 || lToe === -1) return -1
    return sTol + lToe
}