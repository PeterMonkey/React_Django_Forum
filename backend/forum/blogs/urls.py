from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getBlogs),
    path('get/<int:pk>/', views.getBlogById)
]