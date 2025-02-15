function solution(a, b, c, d) {
    const dice = [a, b, c, d];
    const counts = {};

    dice.forEach(num => {
        counts[num] = (counts[num] || 0) + 1;
    });

    const countValues = Object.values(counts).sort((x, y) => y - x);

    if (countValues[0] === 4) {
        return 1111 * a;
    }

    if (countValues[0] === 3) {
        const p = +Object.keys(counts).find(key => counts[key] === 3);
        const q = +Object.keys(counts).find(key => counts[key] === 1);
        return Math.pow(10 * p + q, 2);
    }

    if (countValues[0] === 2 && countValues[1] === 2) {
        const keys = Object.keys(counts).map(Number);
        const p = keys[0];
        const q = keys[1];
        return (p + q) * Math.abs(p - q);
    }

    if (countValues[0] === 2) {
        const keys = Object.keys(counts).map(Number);
        const p = keys.find(key => counts[key] === 2);
        const [q, r] = keys.filter(key => key !== p);
        return q * r;
    }

    return Math.min(...dice);
}