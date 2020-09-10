from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.urls import reverse_lazy
from blog.models import Blog, Comment
from blog import forms
from django.views import View
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

class CreateBlogView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    form_class = forms.CreateBlogForm
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        blog = form.save(commit=False)
        blog.reporter = self.request.user
        blog.slug = slugify(title)
        blog.save()
        return super(CreateBlogView, self).form_valid(form)

    def form_invalid(self, form):
        return super(CreateBlogView, self).form_invalid(form)


class BlogTemplateView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blog.objects.all()
        context["latest_blog"] = blog.order_by("-created_at")[:4]
        context["lifestyle_blog"] = blog.filter(category="0").order_by("-created_at")
        context["fashion_blog"] = blog.filter(category="1").order_by("-created_at")
        context["travel_blog"] = blog.filter(category="2").order_by("-created_at")
        context["fitness_blog"] = blog.filter(category="3").order_by("-created_at")
        context["sports_blog"] = blog.filter(category="4").order_by("-created_at")
        context["popular_blog"] = blog.order_by("-count")
        return context

class BlogCategoryView(LoginRequiredMixin, ListView):
    model = Blog
    ordering = ['-created_at']
    context_object_name = "category_list"
    template_name = "blog/category_blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get('category')
        blog = Blog.objects.all()
        context["latest_blog"] = blog.order_by("-created_at")[:4]
        context["lifestyle_blog"] = blog.filter(category="0").order_by("-created_at")
        context["fashion_blog"] = blog.filter(category="1").order_by("-created_at")
        context["travel_blog"] = blog.filter(category="2").order_by("-created_at")
        context["fitness_blog"] = blog.filter(category="3").order_by("-created_at")
        context["sports_blog"] = blog.filter(category="4").order_by("-created_at")
        context["popular_blog"] = blog.order_by("-count")
        return context

    def get_queryset(self):
        print(self.kwargs)
        category = self.kwargs.get('category')
        category_key = [ item[0] for item in  Blog.CATEGORY if item[1]==category][0]
        return Blog.objects.filter(category=category_key)

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    # success_url = reverse_lazy("blog_detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blog.objects.all()
        context["latest_blog"] = blog.order_by("-created_at")[:4]
        context["lifestyle_blog"] = blog.filter(category="0").order_by("-created_at")
        context["fashion_blog"] = blog.filter(category="1").order_by("-created_at")
        context["travel_blog"] = blog.filter(category="2").order_by("-created_at")
        context["fitness_blog"] = blog.filter(category="3").order_by("-created_at")
        context["sports_blog"] = blog.filter(category="4").order_by("-created_at")
        context["popular_blog"] = blog.order_by("-count")
        context['comments'] = Comment.objects.filter(blog=self.object)
        context['comment_form'] = forms.CommentForm()
        self.object.count = self.object.count +1
        self.object.save()
        return context



def create_comment(request, **kwargs):
    data = request.POST
    blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
    feedback = data.get('feedback')
    comment_by = request.user
    payload = {"blog": blog, "comment_by": comment_by, "feedback":feedback}
    comment = Comment(**payload)
    comment.save()
    return redirect('blog_detail',category=kwargs.get('category'),pk=kwargs.get('pk'),slug = kwargs.get('slug') )



