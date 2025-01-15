function solution(line) {
    const spot = []
    let [minX, maxX, minY, maxY] = [Infinity, -Infinity, Infinity, -Infinity] 
    for (let i = 0; i < line.length; i++) {
        for (let j = i + 1; j < line.length; j++) {
            const [a1, b1, c1] = line[i]
            const [a2, b2, c2] = line[j]
            if (a1 / b1 !== a2 / b2) {
                const x = (b1 * c2 - c1 * b2) / (b2 * a1 - b1 * a2)
                const y = (c1 * a2 - a1 * c2) / (b2 * a1 - b1 * a2)
                if (x === parseInt(x) && y === parseInt(y)) {
                    spot.push([x, y])
                    if (x < minX) minX = x
                    if (x > maxX) maxX = x
                    if (y < minY) minY = y
                    if (y > maxY) maxY = y
                }
            }
        }
    }
    const res = Array.from({ length: maxY - minY + 1 }, () => Array(maxX - minX + 1).fill('.'))
    for (let [x, y] of spot) {
        res[y - minY][x - minX] = '*'
    }
    return res.reverse().map(row => row.join(''))
}