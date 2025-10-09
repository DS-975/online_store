from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Users, Categories
from .templatetags.forms import UsersForm

class HomePageView(TemplateView):
    template_name = 'flatpages/core/default.html'  # Полный путь к шаблону

class UserList(ListView):
    model = Users
    ordering = 'name'
    template_name = 'flatpages/core/users.html'  # Укажите полный путь
    context_object_name = 'users'

class CategoriesDetail(DetailView):
    model = Categories
    template_name = 'flatpages/core/categories.html'
    context_object_name = 'categories'

class UsersCreate(CreateView):
    form_class = UsersForm
    model = Users
    template_name = 'flatpages/core/create_core.html'
    success_url = '/'