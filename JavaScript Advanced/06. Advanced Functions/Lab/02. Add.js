function solution(num) {
    let number = num;

    return add(number)

    function add(numToAdd) {
        number += Number(numToAdd);
    }
}


let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));
