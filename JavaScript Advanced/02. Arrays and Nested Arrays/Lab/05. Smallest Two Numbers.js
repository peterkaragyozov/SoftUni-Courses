function smallestNums(nums) {
    let numbers = nums.sort((a, b) => a - b);
    console.log(numbers[0], numbers[1])
}

smallestNums([30, 15, 50, 5]);
smallestNums([3, 0, 10, 4, 7, 3]);
