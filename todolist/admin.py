from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
