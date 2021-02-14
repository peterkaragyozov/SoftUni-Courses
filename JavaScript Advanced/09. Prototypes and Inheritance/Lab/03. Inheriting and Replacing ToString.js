function personAndTeacher() {
    class Person {
        constructor(name, email) {
            this.name = name;
            this.email = email;
        }

        toString() {
            let output = `${this.constructor.name} (`;
            for (const [key, value] of Object.entries(this)) {
                output += `${key}: ${value}, `;
            }
            output = output.slice(0, -2);
            output += ')';
            return output;
        }
    }

    class Teacher extends Person {
        constructor(name, email, subject) {
            super(name, email);
            this.subject = subject;
        }
    }

    class Student extends Person {
        constructor(name, email, course){
            super(name, email);
            this.course = course;
        }
    }

    return {
        Person,
        Teacher,
        Student
    };
}

const instCreate = personAndTeacher();
const myperson = new instCreate.Person('Peps', 'abv.bg');
const myteacher = new instCreate.Teacher('Pesho Vasilev', 'abv.bg', 'History');
const mystudent = new instCreate.Student('Peps', 'abv.bg', '5');
console.log(myperson.toString());
console.log(myteacher.toString());
console.log(mystudent.toString());
