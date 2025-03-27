function solution(picture, k) {
    return picture.map(p => Array(k).fill(p.replaceAll('.', '.'.repeat(k)).replaceAll('x', 'x'.repeat(k)))).flat()
}