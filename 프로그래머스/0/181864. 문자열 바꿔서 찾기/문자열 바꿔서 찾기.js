function solution(myString, pat) {
    return myString.replace(/A/g, '1')
        .replace(/B/g, '2')
        .includes(pat
                  .replace(/A/g, '2')
                  .replace(/B/g, '1')) ? 1 : 0
}