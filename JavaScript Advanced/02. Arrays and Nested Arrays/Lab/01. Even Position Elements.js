function even(inputArr) {
    let result = '';

    for (let i = 0; i < inputArr.length; i++) {
        if (i % 2 == 0) {
            result += inputArr[i];
            result += ' ';
        }
    }
    console.log(result);
}

even(['20', '30', '40']);
even(['5', '10']);

// Second way

function even(inputArr) {
    let result = [];

    for (let i = 0; i < inputArr.length; i+=2) {
        result[result.length] = inputArr[i];

    }
    return result.join(' ');
}

console.log(even(['20', '30', '40']));
console.log(even(['5', '10']));
