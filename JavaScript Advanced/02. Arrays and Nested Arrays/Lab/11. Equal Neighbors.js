function solve(matrix) {
    let pairs = 0;

    for (let row = 0; row < matrix.length - 1; row++) {
        for (let col = 0; col < matrix[row].length; col++) {

            if (matrix[row][col] === matrix[row + 1][col]) {
                pairs += 1;
            }

        }

    }
    for (let i = 0; i < matrix.length; i++) {
        for (let k = 0; k < matrix[i].length - 1; k++) {
            if (matrix[i][k] === matrix[i][k + 1]) {
                pairs += 1;
            }
            
        }

    }
    
    return pairs;

}


console.log(solve([['test', 'yes', 'yo', 'ho'],
['well', 'done', 'yo', '6'],
['not', 'done', 'yet', '5']]
));
