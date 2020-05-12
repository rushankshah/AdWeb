from django.urls import path
from . import views

app_name = 'adclient'

urlpatterns = [
    path('', views.register_website, name='register_website'),
]