function math(a, b, operator) {
    switch (operator) {
        case '+':
            console.log(a + b);
            break;
        case '-':
            console.log(a - b);
            break;
        case '*':
            console.log(a * b);
            break;
        case '/':
            console.log(a / b);
            break;
        case '%':
            console.log(a % b);
            break;
        case '**':
            console.log(a ** b);
            break;
    }
}

math(5, 6, '+');
math(3, 5.5, '*');
