(function solve() {
    String.prototype.ensureStart = function (str) {
        let currStr = this.toString();
        if (!currStr.startsWith(str)) {
            currStr = str + currStr;
        }
        return currStr;
    };
    String.prototype.ensureEnd = function (str) {
        let currStr = this.toString();
        if (!currStr.endsWith(str)) {
            currStr = this.toString() + str;
        }
        return currStr;
    };
    String.prototype.isEmpty = function () {
        if (this.length == 0 ) {
            return true;
        } else {
            return false;
        }
    };
    String.prototype.truncate = function (n) {
        if (n < 4) {
            return '*'.repeat(n);
        }

        if (this.length > n) {
            const currStr = this.toString();
            const words = currStr.split(' ');
            if (words.length == 1) {
                return currStr.slice(0, n - 3) + '...';
            } else {
               
                let outputStr = '';
                for (const word of words) {
                    const nextLen = outputStr.length + word.length + 3;
                    if (nextLen <= n) {
                        outputStr += word + ' ';
                    } else {
                        outputStr = outputStr.slice(0, -1);
                        outputStr += '...';
                        return outputStr;
                    }
                }
            }
        } else {
            return this.toString();
        }
    };
    String.format = function (string, ...params) {
        const myReg = new RegExp(/{([0-9]*)}/, 'gm');

        let myArr;
        while ((myArr = myReg.exec(string)) != null) {
            const placeholderLength = myArr[0].length;
            const index = Number(myArr[1]);
            if (index >= 0 && index < params.length) {
                string = string.slice(0, myArr.index) + params[index] + ' ' + string.slice(myArr.index + placeholderLength + 1);
            }
        }
        return string;
    };


}());
