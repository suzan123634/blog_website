from django import forms
from blog.models import Blog

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "title", "highlight", "article", "author", "category", "image"