from django.urls import path
from . import views

urlpatterns = [
    path('sellers_ds/', views.seller_profile_detail, name='seller-detail'),
]
