import { html } from '../../node_modules/lit-html/lit-html.js';

import { getAllListings } from '../api/data.js';

const catalogTemplate = (pets) => html`
<section id="dashboard-page" class="dashboard">
    <h1>Dashboard</h1>

    <ul class="other-pets-list">
        ${pets.length == 0 ? html`<p class="no-pets">No pets in database!</p>` : pets.map(miniTemplate)}
    </ul>

</section>`;


export async function catalogPage(ctx) {
    const pets = await getAllListings();
    ctx.render(catalogTemplate(pets));
}

const miniTemplate = (pet) => html`
<li class="otherPet">
    <h3>Name: ${pet.name}</h3>
    <p>Type: ${pet.type}</p>
    <p class="img"><img src="${pet.imageUrl}"></p>
    <a class="button" href="/details/${pet._id}">Details</a>
</li>`;
