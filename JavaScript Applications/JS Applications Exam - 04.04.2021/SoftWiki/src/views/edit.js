import { html } from '../../node_modules/lit-html/lit-html.js';

import { getListingById, updateListing } from '../api/data.js';

const editTemplate = (article, onSubmit) => html`
<section id="edit-page" class="content">
    <h1>Edit Article</h1>

    <form @submit=${onSubmit} id="edit">
        <fieldset>
            <p class="field title">
                <label for="title">Title:</label>
                <input type="text" name="title" id="title" placeholder="Enter article title" .value=${article.title}>
            </p>

            <p class="field category">
                <label for="category">Category:</label>
                <input type="text" name="category" id="category" placeholder="Enter article category" .value=${article.category}>
            </p>
            <p class="field">
                <label for="content">Content:</label>
                <textarea name="content" id="content" .value=${article.content}></textarea>
            </p>

            <p class="field submit">
                <input class="btn submit" type="submit" value="Save Changes">
            </p>

        </fieldset>
    </form>
</section>`;

export async function editPage(ctx) {
    const articleId = ctx.params.id;
    const article = await getListingById(articleId);
    ctx.render(editTemplate(article, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const editedArticle = {
            title: formData.get('title').trim(),
            category: formData.get('category').trim(),
            content: formData.get('content').trim(),
        };


        if (Object.values(editedArticle).some(x => !x)) {
            return alert('All fields are required!');
        }
        
        if ((article.category != "JavaScript") && (article.category != "C#") && (article.category != "Java") && (article.category != "Python")) {
            return alert('The category must be one of JavaScript, C#, Java or Python.');
        }

        await updateListing(articleId, editedArticle);
        event.target.reset();
        ctx.page.redirect('/details/' + articleId);
    }
}
