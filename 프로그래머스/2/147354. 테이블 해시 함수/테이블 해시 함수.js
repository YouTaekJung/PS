const solution = (data, col, row_begin, row_end) => {
    return data
        .sort((a, b) => {
            const [x, y] = [a[col - 1], b[col - 1]];
            return x !== y ? x - y : b[0] - a[0];
        })
        .slice(row_begin - 1, row_end)
        .map((row, i) => row.reduce((acc, cur) => acc + (cur % (row_begin + i)), 0))
        .reduce((res, cur) => res ^ cur, 0);
}