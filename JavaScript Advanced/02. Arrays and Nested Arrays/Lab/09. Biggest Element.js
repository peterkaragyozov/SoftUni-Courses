function solve(matrix) {
    let max_num = -999999;
    for (row=0; row < matrix.length; row++) {
        for (col=0; col < matrix[0].length; col++) {
            if (matrix[row][col] > max_num) {
                max_num = matrix[row][col];
            }
        }
    }
    return max_num
}


console.log(solve(
    [[20, 50, 10],
    [8, 33, 145]]
))

console.log(solve(
    [[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]
))
