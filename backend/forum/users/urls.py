from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.register),
    path('update/', views.putUser),
    path('image/', views.uploadImage),
    path('userProfile/', views.getUserProfile),
    path('soloUser/<int:pk>/', views.getOneUser),
    path('getUsers/', views.getUsers)
]