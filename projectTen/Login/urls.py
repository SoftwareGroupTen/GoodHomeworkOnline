
from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('', views.page, name = 'page'),
    path('login/', views.login, name = 'login'),
]
