from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('site/<int:pk>/', views.site_detail, name='site_detail'),
]
