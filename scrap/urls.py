from django.urls import path,include
from .views import user, List,Api

urlpatterns = [
    path('User/',user),
    path('api/list/', List.as_view(), name='vehicle-list'),
    path('api/vehicles/', Api.as_view(), name='api'),
]