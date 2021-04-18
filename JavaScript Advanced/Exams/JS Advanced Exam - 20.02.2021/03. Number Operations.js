// const expect = require('chai').expect
// const numberOperations = require('./code.js');

//The following code is to be tested:
const numberOperations = {
    powNumber: function (num) {
        return num * num;
    },
    numberChecker: function (input) {
        input = Number(input);

        if (isNaN(input)) {
            throw new Error('The input is not a number!');
        }

        if (input < 100) {
            return 'The number is lower than 100!';
        } else {
            return 'The number is greater or equal to 100!';
        }
    },
    sumArrays: function (array1, array2) {

        const longerArr = array1.length > array2.length ? array1 : array2;
        const rounds = array1.length < array2.length ? array1.length : array2.length;

        const resultArr = [];

        for (let i = 0; i < rounds; i++) {
            resultArr.push(array1[i] + array2[i]);
        }

        resultArr.push(...longerArr.slice(rounds));

        return resultArr
    }
};

// module.exports = numberOperations;


//The following are the mocha and chai unit tests for the presented code above:
describe("BIG TEST", () => {
    describe("powNumber", () => {
        it("SITUATION YES", () => {
            expect(numberOperations.powNumber(2)).to.equal(4);
        });
    });

    describe("numberChecker", () => {
        it("NaN", () => {
            expect(function() { numberOperations.numberChecker('a'); }).to.throw('The input is not a number!');
        });

        it("bellow 100", () => {
            expect(numberOperations.numberChecker(20)).to.equal('The number is lower than 100!');
        });

        it("is 100", () => {
            expect(numberOperations.numberChecker(100)).to.equal('The number is greater or equal to 100!');
        });

        it("over 100", () => {
            expect(numberOperations.numberChecker(120)).to.equal('The number is greater or equal to 100!');
        });
    });

    describe("sumArrays", () => {
        it("SITUATION 1", () => {
            expect(numberOperations.sumArrays([1], [1])).to.deep.equal([2]);
        });

        it("SITUATION 2", () => {
            expect(numberOperations.sumArrays([1, 2, 3], [1, 2, 3])).to.deep.equal([2, 4, 6]);
        });

        it("SITUATION 3", () => {
            expect(numberOperations.sumArrays([1, 2, 3], [1, 2])).to.deep.equal([2, 4, 3]);
        });

        it("SITUATION 4", () => {
            expect(numberOperations.sumArrays([1], [1, 2, 3])).to.deep.equal([2, 2, 3]);
        });

        it("SITUATION 5", () => {
            expect(numberOperations.sumArrays([1, 2, 3], [1])).to.deep.equal([2, 2, 3]);
        });
    });
});
