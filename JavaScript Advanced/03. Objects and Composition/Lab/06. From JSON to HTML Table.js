function fromJSONToHTMLTable(input) {
    let output = '<table>\n   <tr>'
    let jsonAsObj = JSON.parse(input)

    for (let row of Object.keys(jsonAsObj[0])) {
        output += '<th>' + row + '</th>'
    }

    output += '</tr>\n'

    jsonAsObj.forEach((obj) => {
        let values = Object.values(obj);
        output += '   <tr>';
        values.forEach((val) => output += `<td>${val}</td>`)
        output += '</tr>\n';
    })

    output += '</table>'
    console.log(output)
}
