function solution(bandage, health, attacks) {
    let curHealth = health, time = 0, duration = 0
    while (attacks.length) {
        if (attacks[0][0] === time) {
            let damage = attacks[0][1]
            attacks.shift()
            curHealth -= damage
            if (curHealth <= 0) return -1
            duration = 0
        } else {
            duration += 1
            curHealth = Math.min(curHealth + bandage[1], health)
            if (duration === bandage[0]) {
                curHealth = Math.min(curHealth + bandage[2], health)
                duration = 0
            }
        }
        time += 1
    }
    return curHealth
}