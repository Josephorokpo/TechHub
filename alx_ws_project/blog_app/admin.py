from django.contrib import admin
from .models import Category, Blog, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Comment)