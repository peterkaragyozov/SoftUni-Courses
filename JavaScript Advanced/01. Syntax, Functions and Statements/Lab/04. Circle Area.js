function circle(radius) {
    let type = typeof radius;

    if (type == 'number' && Number.isNaN(radius) == false) {
        const area = Math.PI * (radius ** 2);

        console.log(Number(area.toFixed(2)));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${type}.`)
    }
}

circle(5);
circle('name');
