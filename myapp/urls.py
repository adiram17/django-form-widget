from django.urls import path
from . import views

urlpatterns = [
    path('', views.customForm, name='custom-form')
]