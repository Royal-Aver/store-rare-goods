from django.urls import path

from .views import catalog

app_name = 'goods'

urlpatterns = [
    path('catalog', catalog, name='catalog'),
]
