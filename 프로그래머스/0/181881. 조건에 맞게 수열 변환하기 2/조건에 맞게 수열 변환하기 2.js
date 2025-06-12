function solution(arr) {
  let x = 0

  while (true) {
    const nextArr = arr.map(num => {
      if (num >= 50 && num % 2 === 0) {
        return num / 2
      } else if (num < 50 && num % 2 === 1) {
        return num * 2 + 1
      } else {
        return num
      }
    })

    if (arr.every((val, idx) => val === nextArr[idx])) {
      return x
    }

    arr = nextArr
    x++
  }
}
