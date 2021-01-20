function diagonal(matrix) {
    let mainDiag = 0;
    let secDiag = 0;

    for (let i = 0; i < matrix.length; i++) {
        mainDiag += matrix[i][i];
        secDiag += matrix[i][matrix.length - i - 1];
    }
    console.log(mainDiag, secDiag);
}

diagonal([
    [20, 40],
    [10, 60]]
);

diagonal(
    [[3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]]
);
