function solution(my_string, s, e) {
    my_string = my_string.split('')
    return [...my_string.slice(0, s), ...my_string.slice(s, e + 1).reverse(), ...my_string.slice(e + 1) ].join('')
}