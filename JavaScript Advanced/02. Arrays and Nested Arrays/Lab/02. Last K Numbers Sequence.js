function numSeq(...input) {
    let n = Number(input[0]);
    let k = Number(input[1]);
    let nums = [];
    nums[0] = 1

    for (let i = 1; i < n; i++) {
        let sum = 0;
        for (let prev = i - k; prev <= i - 1; prev++) {
            if (prev >= 0) {
                sum += nums[prev];
                nums[i] = sum;
            }
        }
    }
    return nums
}

console.log(numSeq(6, 3));
console.log(numSeq(8, 2));
