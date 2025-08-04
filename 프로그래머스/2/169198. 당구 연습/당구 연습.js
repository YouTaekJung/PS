function solution(m, n, startX, startY, balls) {
    return balls.map(([x, y]) => {
        const ans = []
        if (!(startX === x && startY > y))
            ans.push((startX - x) ** 2 + (startY + y) ** 2)
        if (!(startX === x && startY < y))
            ans.push((startX - x) ** 2 + (2 * n - startY - y) ** 2)
        if (!(startY === y && startX > x))
            ans.push((startX + x) ** 2 + (startY - y) ** 2);
        if (!(startY === y && startX < x))
            ans.push((2 * m - startX - x) ** 2 + (startY - y) ** 2)
        return Math.min(...ans)
  });
}
