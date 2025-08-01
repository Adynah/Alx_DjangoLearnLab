# Update a Book Title

```python
from bookshelf.models import Book

# Retrieve the book by its current title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book.title)

# Expected Output:
# Nineteen Eighty-Four
