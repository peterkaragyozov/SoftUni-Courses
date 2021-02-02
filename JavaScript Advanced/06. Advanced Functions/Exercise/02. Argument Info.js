function solve(...input) {
    const order = {};

    input.forEach(el => {
        console.log(`${typeof el}: ${el}`)

        let key = typeof el;
        order[key] ? order[key] += 1 : order[key] = 1;
    });

    Object.entries(order).sort((a, b) => b[1] - a[1]).forEach(el => {
        console.log(`${el[0]} = ${el[1]}`)
    })
}

solve('cat', 42, function () { console.log('Hello world!'); });
