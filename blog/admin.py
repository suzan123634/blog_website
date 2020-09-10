from django.contrib import admin
from blog.models import Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'category']
    ordering = ['-created_at', 'title']
    list_filter = ['category', 'author']
    date_hierarchy = 'created_at'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)