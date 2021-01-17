function largestNumber(a, b, c) {
    let result;

    if (a > b && a > c) {
        result = a;
    } else if (b > c && b > a) {
        result = b;
    } else {
        result = c;
    }

    console.log(`The largest number is ${result}.`);
}

largestNumber(5, -3, 16);
largestNumber(-3, -5, -22.5);

// Second way:

function largestNumber(a, b, c) {
   console.log(`The largest number is ${Math.max(a, b, c)}.`);
}

largestNumber(5, -3, 16);
largestNumber(-3, -5, -22.5);

// Third way:

function largestNumber(...params) {
    console.log(`The largest number is ${Math.max(...params)}.`);
 }
 
 largestNumber(5, -3, 16);
 largestNumber(-3, -5, -22.5);
 