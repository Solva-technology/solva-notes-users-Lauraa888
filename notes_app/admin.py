from django.contrib import admin
from .models import Note, Category, Status 

admin.site.register(Note)
admin.site.register(Status)
admin.site.register(Category)