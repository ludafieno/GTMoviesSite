from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movieStore.index'),
    path('about/', views.about, name='movieStore.about'),
]