import { html } from '../../node_modules/lit-html/lit-html.js';

import { getAllListings } from '../api/data.js';


const catalogTemplate = (article) => html`
<section id="catalog-page" class="content catalogue">
    <h1>All Articles</h1>

    ${article.length == 0 ? html`<h3 class="no-articles">No articles yet</h3>` : article.map(miniTemplate)}

</section>`;

export async function catalogPage(ctx) {
    const articles = await getAllListings();
    ctx.render(catalogTemplate(articles));
}



const miniTemplate = (article) => html`
<a class="article-preview" href="/details/${article._id}">
    <article>
        <h3>Topic: <span>${article.title}</span></h3>
        <p>Category: <span>${article.category}</span></p>
    </article>
</a>`;
