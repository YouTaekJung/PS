function solution(s) {
    return s.split('').filter(c => s.indexOf(c) === s.lastIndexOf(c)).sort().join('')
}