from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('change_password/', views.change_password, name='accounts.change_password'),
    path('reset_complete/', views.reset_complete, name='accounts.reset_complete'),  # New URL
]