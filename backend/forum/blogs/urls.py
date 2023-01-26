from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getBlogs),
    path('get/<int:pk>/', views.getBlogById),
    path('post/', views.postBlog),
    path('update/<int:pk>/', views.updateBlog),
    path('delete/<int:pk>/', views.deleteBlog),
    path('comment/<int:pk>/', views.createComment)
]