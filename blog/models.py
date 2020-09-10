from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Blog(models.Model):
    CATEGORY =(("0","Lifestyle"),("1","Fashion"),("2","Travel"),("3","Fitness"), ("4", "Sports"))
    title = models.CharField(max_length=150)
    highlight = models.CharField(max_length=300)
    article = models.TextField()
    slug = models.SlugField(max_length=270)
    count = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY, max_length=2)
    image = models.ImageField(upload_to='uploads')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"category": self.get_category_display(), "pk": self.pk, "slug": self.slug})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    feedback = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



