function solution(myString) {
    return myString.split('').map(s => s < 'l' ? 'l' : s).join('')
}