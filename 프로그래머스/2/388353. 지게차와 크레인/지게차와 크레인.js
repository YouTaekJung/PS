const check = (storage, x, y) => {
    const [xlen, ylen] = [storage.length, storage[0].length]
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    const queue = [[x, y]]
    const visited = Array.from({ length: xlen }, () => Array(ylen).fill(0))
    visited[x][y] = 1

    while (queue.length) {
        const cur = queue.shift()
        const [x, y] = cur
        for (let i = 0; i < 4; i++) {
            const [nx, ny] = [x + dx[i], y + dy[i]]
            if (x === 0 || x === xlen - 1
               || y === 0 || y === ylen - 1) {
                return true
            }
            if (0 <= nx && nx < xlen && 0 <= ny && 0 < ylen &&
                !visited[nx][ny] && storage[nx][ny] === '0') {
                queue.push([nx, ny])
                visited[nx][ny] = 1
            }
        }
    }
    return false
}
const solution = (storage, requests) => {
    storage = storage.map(row => row.split(''))
    const [xlen, ylen] = [storage.length, storage[0].length]
    let res = 0
    
    for (let request of requests) {
        const remove = []
        if (request.length === 1) {
            for (let i = 0; i < xlen; i++) {
                for (let j = 0; j < ylen; j++) {
                    if (storage[i][j] === request && check(storage, i, j)) {
                        res += 1
                        remove.push([i, j])
                    }
                }
            }
        } else {
            for (let i = 0; i < xlen; i++) {
                for (let j = 0; j < ylen; j++) {
                    if (storage[i][j] === request[0]) {
                        res += 1
                        remove.push([i, j])
                    }
                }
            }
        }
        
        for (let r of remove) {
            const [x, y] = r
            storage[x][y] = '0'
        }
    }
    return xlen * ylen - res                           
}