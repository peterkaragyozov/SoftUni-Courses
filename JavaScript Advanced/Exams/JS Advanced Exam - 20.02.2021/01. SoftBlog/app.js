function solve() {
    const name = document.getElementById('creator');
    const titleInput = document.getElementById('title');
    const category = document.getElementById('category');
    const content = document.getElementById('content');

    const posts = document.querySelector('div main section');
    const archive = document.querySelector('section ol');

    document.querySelector('button').addEventListener('click', createPost);

    function createPost(event) {
        const title = titleInput.value
        const articleElement = document.createElement('article')
        const headingElement = e('h1', title, 'name');
        const strongCategoryElement = e('strong', category.value);
        const categoryElement = e('p', 'Category:');
        const strongCreatorElement = e('strong', name.value);
        const creatorElement = e('p', 'Creator:')
        const contentElement = e('p', content.value);

        const deleteBtn = e('button', 'Delete', 'btn delete');
        const archiveBtn = e('button', 'Archive', 'btn archive')

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons';
        buttonsDiv.appendChild(deleteBtn);
        buttonsDiv.appendChild(archiveBtn);

        articleElement.appendChild(headingElement);
        categoryElement.appendChild(strongCategoryElement);
        articleElement.appendChild(categoryElement);
        creatorElement.appendChild(strongCreatorElement);
        articleElement.appendChild(creatorElement);
        articleElement.appendChild(contentElement);
        articleElement.appendChild(buttonsDiv);


        deleteBtn.addEventListener('click', () => deleteArticle(name, articleElement));
        archiveBtn.addEventListener('click', () => archiveArticle(title, articleElement));

        posts.appendChild(articleElement);
        event.preventDefault();

    }

    //logic for deleting articles
    function deleteArticle(name, article) {
        article.remove();
    }

    //logic for archiving articles
    function archiveArticle(name, article) {
        article.remove();
        const element = e('li', name);
        archive.appendChild(element);
        sortArchive()
    }

    function sortArchive() {
        Array
            .from(archive.children)
            .sort((a, b) => a.childNodes[0].textContent.localeCompare(b.childNodes[0].textContent))
            .forEach(g => archive.appendChild(g));
    }

    function e(type, content, className) {
        const result = document.createElement(type);
        result.textContent = content;
        if (className) {
            result.className = className;
        }
        return result;
    }
}
