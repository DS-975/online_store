from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('create/', views.UsersCreate.as_view(), name='user_create'),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view(), name='categories_detail'),
]