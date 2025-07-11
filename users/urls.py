from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('order_view/<int:id>', views.order_view, name='order_view'),   
]