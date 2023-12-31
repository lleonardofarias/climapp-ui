from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.index, name='index'), 
    path('get_weather/', views.get_weather, name='get_weather'),
    path('clima/', views.index, name='clima'),  
]
