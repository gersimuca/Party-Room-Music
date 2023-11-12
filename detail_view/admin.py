from django.contrib import admin
from . import models


@admin.register(models.BooksDV)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
