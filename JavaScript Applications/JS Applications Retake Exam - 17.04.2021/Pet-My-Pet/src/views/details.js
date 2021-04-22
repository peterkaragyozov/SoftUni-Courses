import { html } from '../../node_modules/lit-html/lit-html.js';

import { deleteListing, getListingById } from '../api/data.js';

const detailsTemplate = (pet, isOwner, onDelete) => html`
<section id="details-page" class="details">
    <div class="pet-information">
        <h3>Name: ${pet.name}</h3>
        <p class="type">Type: ${pet.type}</p>
        <p class="img"><img src="${pet.imageUrl}"></p>
        <div class="actions">

            ${isOwner ? html`<a class="button" href="/edit/${pet._id}">Edit</a>
            <a class="button" @click=${onDelete} href="javascript:void(0)">Delete</a>` : ''}

        </div>
    </div>
    <div class="pet-description">
        <h3>Description:</h3>
        <p>${pet.description}</p>
    </div>
</section>`;


export async function detailsPage(ctx) {
    const petId = ctx.params.id;
    const pet = await getListingById(petId);
    const isOwner = ctx.user && pet._ownerId == ctx.user._id;
    ctx.render(detailsTemplate(pet, isOwner, onDelete));

    async function onDelete() {
        const confirmed = confirm('Are you sure?');
        if (confirmed) {
            await deleteListing(petId);
            ctx.page.redirect('/all-listings');
        }
    }
}