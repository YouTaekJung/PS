function solution(id_pw, db) {
    for (let [id, pw] of db) {
        if (id_pw[0] !== id) continue
        return id_pw[1] === pw ? 'login' : 'wrong pw'
    }
    return 'fail'
}