# Create a Book Instance

```python
from bookshelf.models import Book
from datetime import date

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=date(1949, 1, 1)
)

