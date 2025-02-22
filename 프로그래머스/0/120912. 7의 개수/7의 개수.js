function solution(array) {
    return array.map(num => '' + num).join('').split('').filter(el => el === '7').length
}