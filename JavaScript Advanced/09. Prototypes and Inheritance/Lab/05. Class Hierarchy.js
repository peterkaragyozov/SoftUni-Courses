function figureCreators() {
    class Figure {
        constructor(units = 'cm') {
            this.units = units;
        }

        get area() { };

        changeUnits(units) {
            this.units = units;
        }

        toString() {
            return `Figure units: ${this.units}`;
        }
    }

    class Circle extends Figure {
        constructor(radius) {
            super();
            this.radius = radius;
        }

        get area() {
            let result = Math.PI * this.radius ** 2;
            if(this.units == 'm'){
                result /= 100;
            } else if(this.units == 'mm') {
                result *= 100;
            }
            return result;
        }

        toString() {
            let rad = this.radius;
            if(this.units == 'm') {
                rad /= 100;
            } else if(this.units =='mm'){
                rad *= 10;
            }
            return `Figures units: ${this.units} Area: ${this.area} - radius: ${rad}`;
        }
    }

    class Rectangle extends Figure {
        constructor(width, height, units) {
            super(units);
            this.width = width;
            this.height = height;
        }

        get area() {
            let result = this.width * this.height;
            if(this.units == 'm'){
                result /= 100;
            } else if(this.units == 'mm') {
                result *= 100;
            }
            return result;
        }

        toString() {
            let wid = this.width;
            let hei = this.height;
            if(this.units =='m'){
                wid /= 100;
                hei /= 100;
            } else if(this.units == 'mm'){
                wid *= 10;
                hei *= 10;
            }

            return `Figures units: ${this.units} Area: ${this.area} - width: ${wid}, height: ${hei}`;
        }
    }

    let circle = new Circle(5);
    console.log(circle.area); // 78.53981633974483
    console.log(circle.toString()); // Figures units: cm Area: 78.53981633974483 - radius: 5

    let rectangle = new Rectangle(3, 4, 'mm');
    console.log(rectangle.area); // 1200 
    console.log(rectangle.toString()); //Figures units: mm Area: 1200 - width: 30, height: 40

    rectangle.changeUnits('cm');
    console.log(rectangle.area); // 12
    console.log(rectangle.toString()); // Figures units: cm Area: 12 - width: 3, height: 4

    circle.changeUnits('mm');
    console.log(circle.area); // 7853.981633974483
    console.log(circle.toString()) // Figures units: mm Area: 7853.981633974483 - radius: 50


    return {
        Figure,
        Circle,
        Rectangle,
    };
}

figureCreators();
