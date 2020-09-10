from django import forms
from blog.models import Blog,Comment

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "title", "highlight", "article", "author", "category", "image"

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('feedback',)