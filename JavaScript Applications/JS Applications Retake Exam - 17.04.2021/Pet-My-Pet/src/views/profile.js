import { html } from '../../node_modules/lit-html/lit-html.js';

import { getMyListings } from '../api/data.js';

const profileTemplate = (pets) => html`
<section id="my-pets-page" class="my-pets">
    <h1>My Pets</h1>

    <ul class="my-pets-list">
        ${pets.length == 0 ? html`<p class="no-pets">No pets in database!</p>` : pets.map(miniTemplate)}
    </ul>

</section>`;

export async function profilePage(ctx) {
    const pets = await getMyListings(ctx.user._id);
    ctx.render(profileTemplate(pets));
}

const miniTemplate = (pet) => html`
<li class="otherPet">
    <h3>Name: ${pet.name}</h3>
    <p>Type: ${pet.type}</p>
    <p class="img"><img src="${pet.imageUrl}"></p>
    <a class="button" href="/details/${pet._id}">Details</a>
</li>`;
