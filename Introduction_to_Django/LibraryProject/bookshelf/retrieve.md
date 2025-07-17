# Retrieve a Book Instance

```python
from bookshelf.models import Book

# Retrieve the book instance by ID
book = Book.objects.get(id=2)

# Display all attributes
print("Title:", book.title)
print("Author:", book.author)
print("Published Date:", book.published_date)

# Expected Output:
# Title: 1984
# Author: George Orwell
# Published Date: 1949-01-01
