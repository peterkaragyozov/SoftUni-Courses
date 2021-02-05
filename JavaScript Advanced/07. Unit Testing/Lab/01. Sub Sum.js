function subSum(arr, start, end) {
    // if the first element is not an array, return NaN
    if (Array.isArray(arr) == false) {
        return NaN;
    }
    // if the start index is less than zero, consider its value to be a zero
    if (start < 0) {
        start = 0;
    }
    // if the end index is outside the bounds of the array, assume it points to the last index
    if (end > arr.length - 1) {
        end = arr.length - 1;
    }

    return arr.slice(start, end + 1).reduce((a, c) => a + Number(c), 0);
}

console.log(subSum([10, 20, 30, 40, 50, 60], 3, 300));
console.log(subSum([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1));
console.log(subSum([10, 'twenty', 30, 40], 0, 2));
console.log(subSum([], 1, 2));
console.log(subSum('text', 0, 2));
