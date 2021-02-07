class Circle {
    constructor(r) {
        this.r = r;
    }

    get radius() {
        return this.r;
    }

    get diameter() {
        return this.r * 2;
    }

    set diameter(value) {
        if (typeof value != 'number') {
            throw new TypeError('Diameter must be a number')
        }
        this.r = value / 2;
    }

    get area() {
        return this.r ** 2 * Math.PI;
    }
}

let c = new Circle(2);
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);
c.diameter = 1.6;
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);
