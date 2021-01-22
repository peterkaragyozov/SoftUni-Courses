const compareNumbers = {
    ascending: (a, b) => a - b,
    descending: (a, b) => b - a,
};

console.log([2, 4, 20, 7, 12, -1, -69, 56, 69, 123, -170].sort(compareNumbers.ascending))


let count = 5;
const parser = {
  increment() { count++; return count},
  decrement() { count--; return count},
  reset() { count = 0; return count}
}

console.log(parser['increment']())

// Second Alternative

let count = 5;
const parser = {
  increment() { count++;},
  decrement() { count--;},
  reset() { count = 0;}
}

parser['increment']()
console.log(count)