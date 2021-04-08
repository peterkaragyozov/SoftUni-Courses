import { html, render } from './node_modules/lit-html/lit-html.js';
import { contacts } from './contacts.js';
import { styleMap } from './node_modules/lit-html/directives/style-map.js';

// Alternatively Row 16 can be as follows:
// <button @click=${onClick} class="detailsBtn">Details</button>
// And in this case Row 25 is to be removed.

const cardTemplate = (data) => html`
<div class="contact card">
    <div>
        <i class="far fa-user-circle gravatar"></i>
    </div>
    <div class="info">
        <h2>Name: ${data.name}</h2>
        <button class="detailsBtn">Details</button>
        <div class="details" id=${data.id} style=${styleMap({display: data.isVisible ? 'block' : 'none'})}>
            <p>Phone number: ${data.phoneNumber}</p>
            <p>Email: ${data.email}</p>
        </div>
    </div>
</div>`;

const container = document.getElementById('contacts');
container.addEventListener('click', onClick);

contacts.forEach(c => c.isVisible = false);
const result = contacts.map(cardTemplate);
render(result, container);

function onClick(event) {
    if (event.target.classList.contains('detailsBtn')) {
        const id = event.target.parentNode.querySelector('.details').id;
        const element = contacts.find(c => c.id == id);
        element.isVisible = !element.isVisible;
        const result = contacts.map(cardTemplate);
        render(result, container);
    } 

    /*

    // Second way:
    const element = event.target.parentNode;
    const currentStyle = element.querySelector('.details').style.display;
    if (currentStyle == 'block') {
        element.querySelector('.details').style.display = 'none';
    } else {
        element.querySelector('.details').style.display = 'block';
    }

    */

}
