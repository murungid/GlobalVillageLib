from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Category, Book, Bookcopy, BorrowRecord
from .forms import (
    BookForm,
    BookcopyForm,
    BorrowRecordForm,
    CategoryForm,
    MemberForm,
)
from django.contrib import messages

#dashboard
def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {"books": books})

#listing all the books
def book_list(request):
    books = Book.objects.all()
    return render(request,"books/book_list.html",{
        "books" : books,
        "total": books.count()
    })


# getting the book details
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_details.html", {"book": book})



# creating a new book
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added a new book")
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form, "title": "Add New Book"})


# book update
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully updated the book")
            return redirect("home")
    else:
        form = BookForm(instance=book)
    return render(
        request,
        "books/book_form.html",
        {"form": form, "title": "Update Book"},
    )

#book delete
def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request,"books/book_delete.html",{
        'book': book
    })




# creating new members
def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created a new member")
            return redirect("home")
    else:
        form = MemberForm()
    return render(request, "books/create_member.html", {"form": form})

#creating the different categories

def create_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created new category ")
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request,"books/create_categories.html",{
        "form" : form 
    })
