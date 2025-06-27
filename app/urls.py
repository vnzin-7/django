from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
]
