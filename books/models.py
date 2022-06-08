# /app_name/models.py
from django.db import models


class Author:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Book:
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)  # khóa ngoại đến bảng `authors`

    def __str__(self):
        return f"{self.id}: {self.title}"
