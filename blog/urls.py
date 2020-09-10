from django.urls import path
from blog import views


urlpatterns = [
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.CreateBlogView.as_view(), name="create_blog"),
    path('<str:category>/', views.BlogCategoryView.as_view(), name="category_blog"),
    path('<str:category>/<int:pk>/<str:slug>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('<str:category>/<int:pk>/<str:slug>/comment/', views.create_comment, name="create_comment"),
]