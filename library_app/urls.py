from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_view),
    path('author/', views.author_view),
    path('category/', views.category_view),
]
