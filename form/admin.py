from django.contrib import admin
from .models import Author, Book


class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]
    model = Author

admin.site.register(Author, AuthorAdmin)
