from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('post/<int:id>/', views.post_detail, name='post_detail'),

    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]