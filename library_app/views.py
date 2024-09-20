from django.shortcuts import HttpResponse
from .models import Book, Author, Category


def book_view(requests):
    books = Book.objects.all()
    response = ""
    for book in books:
        response += f"""

            <h2>{book.title}</h2>

"""

        response += f"""

            <ul>
            <li>{book.author}</li>
            <li>{book.category}</li>            
            <li>{book.created_day}</li>
            <li>{book.updated_day}</li>
            </ul>

"""

    return HttpResponse(response)


def author_view(requests):
    authors = Author.objects.all()
    response = ""
    for author in authors:
        response += f"""

            <h2>{author.full_name}</h2>

"""

        response += f"""

            <ul>
            <li>{author.bio}</li>
            </ul>

"""

    return HttpResponse(response)


def category_view(requests):
    categorys = Category.objects.all()
    response = ""
    for category in categorys:
        response += f"""

            <h2>{category.name}</h2>

"""

        response += f"""

            <ul>
            <li>{category.description}</li>
            </ul>

"""

    return HttpResponse(response)
