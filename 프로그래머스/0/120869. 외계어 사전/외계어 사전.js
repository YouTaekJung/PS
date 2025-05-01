function solution(spell, dic) {
    return  !dic.filter(word => spell.every(s => word.includes(s))).length + 1
}