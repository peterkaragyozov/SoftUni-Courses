function solve(input, ...rest) {

    let arr = input;
    let start = rest[0];
    let end = rest[1];
    let start_idx = Number(arr.indexOf(start));
    let end_idx = Number(arr.indexOf(end, start_idx));

    return arr.slice(start_idx, end_idx + 1);
}


console.log(solve(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'
))

console.log(solve(['Apple Crisp',
'Mississippi Mud Pie',
'Pot Pie',
'Steak and Cheese Pie',
'Butter Chicken Pie',
'Smoked Fish Pie'],
'Pot Pie',
'Smoked Fish Pie'
))
