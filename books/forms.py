from django import forms
from .models import Book, Category, Member, Bookcopy, BorrowRecord


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "subtitle",
            "authors_name",
            "isbn",
            "edition",
            "publication_year",
            "description",
            "categories",
        ]
        widgets = {
            "categories": forms.CheckboxSelectMultiple,
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categories"].queryset = Category.objects.all().order_by("name")


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "muru****@gmail.com"}),
        }


class BookcopyForm(forms.ModelForm):
    class Meta:
        model = Bookcopy
        fields = ["book", "copy_number", "condition", "acquisition_date", "status"]
        widgets = {
            "acquisition_date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = [
            "member",
            "book_copy",
            "due_date",
            "return_date",
            "fine_amount",
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"}),
        }
