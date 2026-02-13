import os
import django
from django.test import Client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()


def verify_view():
    client = Client()
    response = client.get("/books/home/")

    if response.status_code == 200:
        print("View accessed successfully (Status 200).")
        content = response.content.decode()
        if "Book List" in content and "Harry Potter" in content:
            print("Content verification successful.")
        else:
            print("Content verification failed.")
            print(content)
    else:
        print(f"View access failed with status {response.status_code}.")


if __name__ == "__main__":
    verify_view()
