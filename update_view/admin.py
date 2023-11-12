from django.contrib import admin
from . import models


@admin.register(models.BooksUV)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }