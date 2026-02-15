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


# dashboard
def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {"books": books})


# listing all the books
def book_list(request):
    books = Book.objects.all()
    return render(
        request, "books/book_list.html", {"books": books, "total": books.count()}
    )


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
    return render(
        request, "books/book_form.html", {"form": form, "title": "Add New Book"}
    )


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


# book delete
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_delete.html", {"book": book})


# creating new members
def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created a new member")
            return redirect("list_members")
    else:
        form = MemberForm()
    return render(request, "books/create_member.html", {"form": form})


# listing all the members
def list_members(request):
    members = Member.objects.all()
    return render(request, "books/list_members.html", {"members": members})


# member details
def member_details(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, "books/member_details.html", {"member": member})


# member delete
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
    return render(request, "books/member_delete.html", {"member": member})


# member  update
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("list_members")
    else:
        form = MemberForm(instance=member)
    return render(
        request, "books/member_update.html", {"form": form, "title": "Update Member"}
    )


# creating the different categories
def create_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created new category ")
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "books/create_categories.html", {"form": form})


# categories list
def category_list(request):
    categories = Category.objects.all()
    return render(request, "books/category_list.html", {"categories": categories})


# details for categories
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, "books/category_detail.html", {"category": category})


# categories update
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(
        request,
        "books/category_update.html",
        {"form": form, "title": "Categoty Update"},
    )


# categories delete
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "books/category_delete.html", {"category": category})


# bookcopy this entiles of the copies of books available,thier status plus accounts
# for the material of the books
# boocopy list
def list_bookcopy(request):
    bookcopy = Bookcopy.objects.all()
    return render(request, "books/list_bookcopy.html", {"bookcopy": bookcopy})

#bookcopy create 
def create_bookcopy(request):
    if request.method == "POST":
            form = BookcopyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("list_bookcopy")
    else:
        form = BookcopyForm()
    return render(request,"books/create_bookcopy.html",{
        "form" : form
    })

#bookcopy details
def details_bookcopy(request,pk):
    bookcopy = get_object_or_404(Bookcopy,pk=pk)
    return render(request,"books/details_bookcopy",{
        "bookcopy" : bookcopy
    })
#bookcopy delete
def delete_bookcopy(request,pk):
    bookcopy = get_object_or_404(Bookcopy,pk=pk)
    if request.method == "POST":
        bookcopy.delete()
        return redirect("list_bookcopy")
    return render(request,"books/delete_bookycopy.html")

#update update
def update_bookcopy(request,pk):
    bookcopy = get_object_or_404(Bookcopy,pk=pk)
    if request.method == "POST":
        form = BookcopyForm(request.POST,instance=bookcopy)
        if form.is_valid():
            form.save()
            return redirect("list_bookcopy")
    else:
        form = BookcopyForm(instance=bookcopy)
    return render(request,"books/update_bookcopy.html",{
        "form" : form
    })


