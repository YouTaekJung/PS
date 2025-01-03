const isValid = (park, x, y) => {
    const xlen = park.length
    const ylen = park[0].length
    if (x < 0 || x >= xlen) return false
    if (y < 0 || y >= ylen) return false
    if (park[x][y] === 'X') return false
    return true
}

const solution = (park, routes) => {
    let x,y
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    const d = 'NSWE'
    
    for (let i = 0; i < park.length; i++) {
        for (let j = 0; j < park[i].length; j++) {
            if (park[i][j] === 'S') {
                [x, y] = [i, park[i].indexOf('S')]
            }
        }
    }
    
    for (let route of routes) {
        const [op, n] = route.split(' ')
        const dIdx = d.indexOf(op)
        
        let check = true
        for (let i = 1; i <= n; i++) {
            const [nx, ny] = [x + dx[dIdx] * i, y + dy[dIdx] * i]
            if (!isValid(park, nx, ny)) check = false
        }
        if (check) {
            [x, y] = [x + dx[dIdx] * n, y + dy[dIdx] * n]
        }
    }
    return [x, y]
}