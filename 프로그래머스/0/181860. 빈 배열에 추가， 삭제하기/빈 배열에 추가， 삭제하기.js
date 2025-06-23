function solution(arr, flag) {
  const res = []

  for (let i = 0; i < arr.length; i++) {
    if (flag[i]) {
      for (let j = 0; j < arr[i] * 2; j++) {
        res.push(arr[i])
      }
    } else {
      res.splice(-arr[i], arr[i])
    }
  }

  return res
}