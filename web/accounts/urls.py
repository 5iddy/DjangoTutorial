from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.register_page, name="login"),
]