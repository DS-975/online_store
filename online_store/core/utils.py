from django.urls import path, include
# Импортируем созданное нами представление
from . import views
from .views import PostList, PostDetail, create_post, PostCreate, PostUpdate, PostDelete, Online_Store

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('', PostList.as_view(), name='sorting'),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('test/', PostCreate.as_view(), name='test'),

   path('online_store/', Online_Store.as_view(), name='online_store'),
]