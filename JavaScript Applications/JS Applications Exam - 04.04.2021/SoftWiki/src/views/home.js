import { html } from '../../node_modules/lit-html/lit-html.js';

import { getAllRecentListings } from '../api/data.js';


const homeTemplate = (javascript, csharp, java, python) => html`
<section id="home-page" class="content">
    <h1>Recent Articles</h1>
    <section class="recent js">
        <h2>JavaScript</h2>
        ${javascript.length == 0 ? html`<h3 class="no-articles">No articles yet</h3>` : javascript.map(miniArticleTemplate)}
    </section>
    <section class="recent csharp">
        <h2>C#</h2>
        ${csharp.length == 0 ? html`<h3 class="no-articles">No articles yet</h3>` : csharp.map(miniArticleTemplate)}
    </section>
    <section class="recent java">
        <h2>Java</h2>
        ${java.length == 0 ? html`<h3 class="no-articles">No articles yet</h3>` : java.map(miniArticleTemplate)}
    </section>
    <section class="recent python">
        <h2>Python</h2>
        ${python.length == 0 ? html`<h3 class="no-articles">No articles yet</h3>` : python.map(miniArticleTemplate)}
    </section>
</section>`;

export async function homePage(ctx) {
    const articles = await getAllRecentListings();
    const javascript = articles.filter(article => article.category == "JavaScript");
    const csharp = articles.filter(article => article.category == "C#");
    const java = articles.filter(article => article.category == "Java");
    const python = articles.filter(article => article.category == "Python")
    ctx.render(homeTemplate(javascript, csharp, java, python));
}

const miniArticleTemplate = (articleType) => html`
<article>
    <h3>${articleType.title}</h3>
    <p>${articleType.content}</p>
    <a href="/details/${articleType._id}" class="btn details-btn">Details</a>
</article>`;
