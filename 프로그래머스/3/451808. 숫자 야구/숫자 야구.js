function solution(n, submit) {
  const digits = Array(9).fill(1).map((el, i) => el + i)
  const candidates = []

  function permute(prefix, remaining) {
    if (prefix.length === 4) {
      candidates.push(prefix.join(''))
      return
    }
    for (let i = 0; i < remaining.length; i++) {
      permute([...prefix, remaining[i]], remaining.filter((_, idx) => idx !== i))
    }
  }

  permute([], digits)

  function getHint(secret, guess) {
    let s = 0, b = 0
    for (let i = 0; i < 4; i++) {
      if (secret[i] === guess[i]) s++
      else if (secret.includes(guess[i])) b++
    }
    return `${s}S ${b}B`
  }

  while (candidates.length > 1) {
    const guess = candidates[0]
    const result = submit(Number(guess))
    candidates.splice(0, candidates.length, ...candidates.filter(c => getHint(c, guess) === result))
  }

  return Number(candidates[0])
}
