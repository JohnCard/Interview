from django.urls import path,include
from .views import hello, user

urlpatterns = [
    path('hello/',hello),
    path('User/',user)
]