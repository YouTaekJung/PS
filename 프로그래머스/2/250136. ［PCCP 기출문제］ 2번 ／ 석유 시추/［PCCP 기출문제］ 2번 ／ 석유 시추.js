const bfs = (land, visited, cur, i, j) => {
    const dx = [-1, 0, 1, 0]
    const dy = [0, -1, 0, 1]
    const queue = [[i, j]]
    let count = 0;

    while (queue.length) {
        const [x, y] = queue.shift()
        visited[x][y] = 1
        land[x][y] = cur
        for (let k = 0; k < 4; k++) {
            const [nx, ny] = [x + dx[k], y + dy[k]]
            if (0 <= nx && nx < land.length
                && 0 <= ny && ny < land[0].length
                && visited[nx][ny] === 0
                && land[nx][ny] === 1) {
                visited[nx][ny] = 1
                queue.push([nx, ny])
            }
        }
        count += 1
    }
    return count 
}

const solution = (land) => {
    const visited = Array.from({ length: land.length }, () => Array(land[0].length).fill(0));
    const amount = {}
    let cur = 2
    
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[i].length; j++) {
            if (land[i][j] === 1 && visited[i][j] === 0) {
                amount[cur] = bfs(land, visited, cur, i, j)
                visited[i][j] = 1
                cur += 1
            }
        }
    }
    
    let res = 0
    for (let i = 0; i < land[0].length; i++) {
        const area = new Set()
        for (let j = 0; j < land.length; j++) {
            if (land[j][i] > 1) area.add(land[j][i])
        }
        const currentSum = [...area].reduce((acc, cur) => acc + amount[cur], 0)
        res = Math.max(res, currentSum)
    }
    return res
}