function solution(cipher, code) {
    return cipher.split('').filter((_, idx) => idx % code === code - 1).join('')
}