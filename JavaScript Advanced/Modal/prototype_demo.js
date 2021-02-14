function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

const myProto = {
    write(message) {
        console.log(`${this.firstName} wrote: ${message}`);
    }
};

/*
Person.prototype.write = function(message) {
    console.log(`${this.firstName} wrote: ${message}`);
};
*/

/*
const myPerson = new Person('John', 'Abbot');
const otherPerson = new Person('Peter', 'Jackson');
*/

function newOperator(constructor, ...params) {
    // allocate memory and assign prototype
    const result = Object.create(myProto);
    //const result = Object.create(constructor.prototype);

    // execute constructor with params inside memory context
    constructor.apply(result, params);

    // return memory reference
    return result;
}

const myPerson = newOperator(Person, 'John', 'Abbot');
const otherPerson = newOperator(Person, 'Peter', 'Jackson');

console.log(myPerson, otherPerson);


myPerson.write('hello');
otherPerson.write('hi');

console.log(myPerson.write == otherPerson.write);
