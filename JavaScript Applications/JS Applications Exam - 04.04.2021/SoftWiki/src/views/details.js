import { html } from '../../node_modules/lit-html/lit-html.js';

import { deleteListing, getListingById } from '../api/data.js';


const detailsTemplate = (article, isOwner, onDelete) => html`
<section id="details-page" class="content details">
    <h1>${article.title}</h1>

    <div class="details-content">
        <strong>Published in category ${article.category}</strong>
        <p>${article.content}</p>

        ${isOwner ? html`<div class="buttons">
            <a @click=${onDelete} href="javascript:void(0)" class="btn delete">Delete</a>
            <a href="/edit/${article._id}" class="btn edit">Edit</a>           
        </div>` : html`<a href="/" class="btn edit">Back</a>`}

        
    </div>
</section>`;

export async function detailsPage(ctx) {
    const articleId = ctx.params.id;
    const article = await getListingById(articleId);
    const isOwner = ctx.user && article._ownerId == ctx.user._id;
    ctx.render(detailsTemplate(article, isOwner, onDelete));


    async function onDelete() {
        const confirmed = confirm('Are you sure?');
        if (confirmed) {
            await deleteListing(articleId);
            ctx.page.redirect('/');
        }
    }
}

