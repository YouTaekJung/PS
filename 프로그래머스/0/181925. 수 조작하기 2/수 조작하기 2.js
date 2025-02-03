function solution(numLog) {
    let res = ''
    const hash = { '1': 'w', '-1': 's', '10': 'd', '-10': 'a' }
    for (let i = 1; i < numLog.length; i++) {
        res += hash[String(numLog[i] - numLog[i - 1])]
    }
    return res
}