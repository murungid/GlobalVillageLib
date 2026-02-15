from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("create_book/", views.book_create, name="book_create"),
    path("create_member/", views.create_member, name="create_member"),
    path("book/<int:pk>/update/", views.book_update, name="book_update"),
    path("books/", views.book_list, name="book_list"),
    path("book/<int:pk>/delete/", views.book_delete, name="book_delete"),
    path("create_categories/", views.create_categories, name="create_categories"),
    path("list_members/", views.list_members, name="list_members"),
    path("member/<int:pk>/", views.member_details, name="member_details"),
    path("member/<int:pk>delete/", views.member_delete, name="member_delete"),
    path("member/<int:pk>/update/", views.member_update, name="member_update"),
    path("category_list/", views.category_list, name="category_list"),
    path("category/<int:pk>", views.category_detail, name="category_detail"),
    path("category/<int:pk>/update/", views.category_update, name="category_update"),
    path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),
    #bookcopies
    path("list_bookcopy/",views.list_bookcopy,name="list_bookcopy")
]
