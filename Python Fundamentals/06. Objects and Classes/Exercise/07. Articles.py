class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, content):
        self.content = content
        return self.content

    def change_author(self, author):
        self.author = author
        return self.author

    def rename(self, title):
        self.title = title
        return self.title

    def __repr__(self):
        return f"{self.title} = {self.content}: {self.author}"

article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)