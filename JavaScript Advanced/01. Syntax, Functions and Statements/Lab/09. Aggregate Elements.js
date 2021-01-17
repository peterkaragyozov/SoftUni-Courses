function aggr(input) {
    console.log(reduce(input, (acc, c) => acc + c, 0));
    console.log(reduce(input, (acc, c) => acc + 1/c, 0));
    console.log(reduce(input, (acc, c) => acc + c, ''));

    function reduce(arr, operator, initialVal) {
        let current = initialVal;

        for (let i = 0; i < arr.length; i++) {
            current = operator(current, arr[i]);
        }
        return current;
    }
}

aggr([1, 2, 3]);
aggr([2, 4, 8, 16]);

// Second way

function aggr(input) {
    console.log(input.reduce((acc, c) => acc + c, 0));
    console.log(input.reduce((acc, c) => acc + 1/c, 0));
    console.log(input.reduce((acc, c) => acc + c, ''));
}

aggr([1, 2, 3]);
aggr([2, 4, 8, 16]);
