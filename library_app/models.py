from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=300)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_day = models.DateTimeField(auto_now_add=True)
    updated_day = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
