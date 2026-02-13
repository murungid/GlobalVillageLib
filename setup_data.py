import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from books.models import Book, Author


def setup_data():
    if not Book.objects.exists():
        author1 = Author.objects.create(first_name="J.K.", last_name="Rowling")
        author2 = Author.objects.create(first_name="George", last_name="Orwell")

        book1 = Book.objects.create(
            title="Harry Potter", isbn=1234567890, publication_year=1997
        )
        book1.authors.add(author1)

        book2 = Book.objects.create(
            title="1984", isbn=9876543210, publication_year=1949
        )
        book2.authors.add(author2)

        print("Data created successfully.")
    else:
        print("Data already exists.")


if __name__ == "__main__":
    setup_data()
