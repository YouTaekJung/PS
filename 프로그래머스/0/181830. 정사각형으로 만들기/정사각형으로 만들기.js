function solution(arr) {
    const rows = arr.length;
    const cols = arr[0].length;

    if (rows > cols) {
        arr = arr.map(row => [...row, ...Array(rows - cols).fill(0)]);
    } else if (cols > rows) {
        for (let i = 0; i < cols - rows; i++) {
            arr.push(Array(cols).fill(0));
        }
    }
    return arr;
}
