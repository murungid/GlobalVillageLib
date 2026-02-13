from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    authors_name = models.CharField(max_length=64, blank=False, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    edition = models.CharField(max_length=64, blank=True, null=True)
    publication_year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Bookcopy(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("borrowed", "Borrowed"),
        ("reserved", "Reserved"),
        ("lost", "Lost"),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    copy_number = models.CharField(max_length=64)
    condition = models.CharField(max_length=64, blank=True, null=True)
    acquisition_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=64, choices=STATUS_CHOICES, default="available"
    )

    def __str__(self):
        return f"{self.book.title} {self.copy_number}"

    class Meta:
        verbose_name_plural = "Book copies"


class Member(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(Bookcopy, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    fine_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.member} borrowed {self.book_copy}"

    class Meta:
        ordering = ["-borrow_date"]
