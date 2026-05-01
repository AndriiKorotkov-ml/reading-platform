from content.base import Content
from content.article import Article
from content.book import Book
from content.poem import Poem
contents = [Book(),Poem(),Article()]
for content in contents:
    print(content.display())

