# CRUD Operations Using Django Shell

## 📌 Create

```python
from bookshelf.models import Book
from datetime import date

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=date(1949, 1, 1)
)
print(book)
# Output: 1984

```
## Retrieve

```python
book = Book.objects.get(title="1984")
print("Title:", book.title)
print("Author:", book.author)
print("Published Date:", book.published_date)
# Output:
# Title: 1984
# Author: George Orwell
# Published Date: 1949-01-01


```
## Update

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four


```
## Delete

```python
book.delete()
all_books = Book.objects.all()
print(list(all_books))
# Output: []

