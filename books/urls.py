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
    path("create_categories/",views.create_categories,name="create_categories")

]
