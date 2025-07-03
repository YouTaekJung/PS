function solution(sides) {
    return sides.reduce((a, b) => a + b) > 2 * Math.max(...sides) ? 1 : 2
}