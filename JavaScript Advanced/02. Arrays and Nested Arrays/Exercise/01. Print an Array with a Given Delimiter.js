const solve = (arr, delimiter) => {
    let result = '';

    for (let i = 0; i < arr.length; i++) {
        result += i==arr.length-1 ? arr[i] : (arr[i] + delimiter);
    }
    return result;
}

console.log(solve(['One', 
'Two', 
'Three', 
'Four', 
'Five'], 
'-'
));

console.log(solve(['How about no?', 
'I',
'will', 
'not', 
'do', 
'it!'], 
'_'
));


// Second way

const solve = (arr, delimiter) => arr.join(delimiter);

console.log(solve(['One', 
'Two', 
'Three', 
'Four', 
'Five'], 
'-'
));

console.log(solve(['How about no?', 
'I',
'will', 
'not', 
'do', 
'it!'], 
'_'
));
