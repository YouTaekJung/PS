const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));

const gcdOfArray = (nums) => nums.reduce((acc, num) => gcd(acc, num));

function solution(arrayA, arrayB) {
    const [gcdA, gcdB] = [gcdOfArray(arrayA), gcdOfArray(arrayB)]
    let res = []
    if (arrayA.every(num => num % gcdB !== 0)) res.push(gcdB)
    if (arrayB.every(num => num % gcdA !== 0)) res.push(gcdA)
    return res.length ? Math.max(...res) : 0
}