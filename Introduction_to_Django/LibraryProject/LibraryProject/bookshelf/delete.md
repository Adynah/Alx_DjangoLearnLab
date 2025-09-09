# Delete a Book Instance

```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by retrieving all books
all_books = Book.objects.all()
print(list(all_books))

# Expected Output:
# []
# (An empty list means the book was successfully deleted.)
