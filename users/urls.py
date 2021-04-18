from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.simple_html_view),
    path('users/', views.list_users),
]