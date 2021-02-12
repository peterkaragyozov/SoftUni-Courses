function solve(input) {
    let parse = JSON.parse(input)
    let str = '<table>\n'
    str += `   <tr>${Object.keys(parse[0]).map(x => `<th>${replace(x)}</th>`).join('')}</tr>\n` 
    parse.forEach( x => { str += `   <tr>${Object.values(x).map( x => `<td>${replace(x)}</td>`).join('')}</tr>\n` })
    str += '</table>'

    
    function replace(str) {
        return String(str)
            .replace(/&/g , '&amp;')
            .replace(/</g , "&lt;")
            .replace(/>/g , "&gt;")
            .replace(/"/g , "&quot;")
            .replace(/'/g , "&#39;")
    }
    return str
}


// Second way

// function fromJSONToHTMLTable(input) {
//     let output = '<table>\n   <tr>'
//     let jsonAsObj = JSON.parse(input)

//     for (let row of Object.keys(jsonAsObj[0])) {
//         output += '<th>' + row + '</th>'
//     }

//     output += '</tr>\n'

//     jsonAsObj.forEach((obj) => {
//         let values = Object.values(obj);
//         output += '   <tr>';
//         values.forEach((val) => output += `<td>${val}</td>`)
//         output += '</tr>\n';
//     })

//     output += '</table>'
//     console.log(output)
// }
