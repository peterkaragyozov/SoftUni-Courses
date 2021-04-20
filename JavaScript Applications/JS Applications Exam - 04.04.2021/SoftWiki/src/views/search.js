import { html } from '../../node_modules/lit-html/lit-html.js';

import { search } from '../api/data.js';

const searchTemplate = (articles, onSearch, title) => html`
<section id="search-page" class="content">
    <h1>Search</h1>
    <form @submit=${onSearch} id="search-form">
        <p class="field search">
            <input id="search-input" type="text" placeholder="Search by article title" name="search">
        </p>
        <p class="field submit">
            <input id="submit" class="btn submit" type="submit" value="Search">
        </p>
    </form>
    <div class="search-container">
        
        ${(articles.length == 0 || title == '') ? html`<h3 class="no-articles">No matching articles</h3>` : articles.map(miniTemplate)}
        
    </div>
</section>`;

export async function searchPage(ctx) {
    // const title = ctx.querystring.split('=')[1];
    // const articles = await search(title);
    // ctx.render(searchTemplate(articles, onSearch, title));

    updateView(false);

    function updateView(showResults, articles = [], title){
        ctx.render(searchTemplate(articles, onSearch, title));
    }

    async function onSearch(ev){
        ev.preventDefault();
        const formData = new FormData(ev.target);
        const match = formData.get('search');
        const articles = await search(match)
        updateView(true, articles, match);
    }
}


const miniTemplate = (article) => html`
<a class="article-preview" href="/details/${article._id}">
    <article>
        <h3>Topic: <span>${article.title}</span></h3>
        <p>Category: <span>${article.category}</span></p>
    </article>
</a>`;
