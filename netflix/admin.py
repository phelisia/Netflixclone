from django.contrib import admin
from django.test import tag

from netflix.models import Category, Movie,Tag

# Register your models here.
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)
