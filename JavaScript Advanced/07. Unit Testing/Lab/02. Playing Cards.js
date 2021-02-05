function createCard(face, suit) {
    const validFaces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    const suitToString = {
        'S': '\u2660',
        'H': '\u2665',
        'D': '\u2666',
        'C': '\u2663',    
    };

    if (validFaces.includes(face) == false) {
        throw new Error('Invalid face');
    } else if (Object.keys(suitToString).includes(suit) == false) {
        console.log(Object.keys(suitToString));
        throw new Error('Invalid suit');
    }

    return {
        face,
        suit,
        toString () {
            return `${face}${suitToString[suit]}`;
        }
    };
}

console.log(createCard('A', 'S'));
console.log(createCard('10', 'H'));
console.log(createCard('1', 'C'));
