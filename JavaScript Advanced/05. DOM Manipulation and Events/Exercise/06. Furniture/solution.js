function solve() {
  const textareas = document.querySelectorAll('textarea');
  const buttons = document.querySelectorAll('button');
  const body = document.querySelector('tbody');

  // create rows in the table for every furniture

  buttons[0].addEventListener('click', function (e) {
    const arr = JSON.parse(textareas[0].value);

    for (el of arr) {
      const row = document.createElement('tr');

      // create image cell
      
      const cellImage = document.createElement('td');
      const image = document.createElement('img');
      image.setAttribute('src', el.img);
      cellImage.appendChild(image);

      const cellName = document.createElement('td');
      const pName = document.createElement('p');
      pName.textContent = el.name;
      cellName.appendChild(pName);

      const cellPrice = document.createElement('td');
      const pPrice = document.createElement('p');
      pPrice.textContent = el.price;
      cellPrice.appendChild(pPrice);

      const cellDecor = document.createElement('td');
      const pDecor = document.createElement('p');
      pDecor.textContent = el.decFactor;
      cellDecor.appendChild(pDecor);

      const cellCheck = document.createElement('td');
      const input = document.createElement('input');
      input.setAttribute('type', 'checkbox');
      cellCheck.appendChild(input);


      row.appendChild(cellImage);
      row.appendChild(cellName);
      row.appendChild(cellPrice);
      row.appendChild(cellDecor);
      row.appendChild(cellCheck);

      body.appendChild(row);
    }
  })

  buttons[1].addEventListener('click', function (e) {
    const furniture = Array.from(body.querySelectorAll('input[type=checkbox]:checked')).map(input => input.parentNode.parentNode);

    const result = {
      bought: [],
      totalPrice: 0,
      decFactorSum: 0
    }

    for (let row of furniture) {
      const cells = row.children;

      const name = cells[1].children[0].textContent;
      result.bought.push(name);

      const price = Number(cells[2].children[0].textContent);
      result.totalPrice += price;

      const factor = Number(cells[3].children[0].textContent);
      result.decFactorSum += factor;
    }

      textareas[1].value = `Bought furniture: ${result.bought.join(', ')}\nTotal price: ${result.totalPrice.toFixed(2)}\nAverage decoration factor: ${(result.decFactorSum / furniture.length)}`
  
  })
}


// //  Second Way

// function solve() {
//   const [input, output] = [...document.querySelectorAll('textarea')];
//   const table = document.querySelector('table.table tbody');
//   const [generateBtn, buyBtn] = [...document.querySelectorAll('button')];

//   const furniture = [];

//   generateBtn.addEventListener('click', () => {
//       const furnitureArray = JSON.parse(input.value.trim());
//       table.innerHTML = '';
//       furnitureArray.forEach(f => {
//           const item = createRow(f);
//           furniture.push(item);
//           table.appendChild(item.element);
//       });
//   });

//   buyBtn.addEventListener('click', () => {
//       furniture.forEach(f => console.log(f.getValues().name, f.isChecked()));
//   });

//   const td = e.bind(null, 'td');

//   function createRow(data) {
//       const img = e('img');
//       img.src = data.img;

//       const check = e('input');
//       check.type = 'checkbox';

//       const element = e('tr',
//           td(img),
//           td(e('p', data.name)),
//           td(e('p', data.price)),
//           td(e('p', data.decFactor)),
//           td(check)
//       );

//       return {
//           element,
//           isChecked,
//           getValues
//       };

//       function isChecked() {
//           return check.checked;
//       }

//       function getValues() {
//           return data;
//       }
//   }

//   function e(type, ...content) {
//       const result = document.createElement(type);

//       content.forEach(e => {
//           if (typeof e == 'string') {
//               const node = document.createTextNode(e);
//               result.appendChild(node);
//           } else {
//               result.appendChild(e);
//           }
//       });

//       return result;
//   }
// }
