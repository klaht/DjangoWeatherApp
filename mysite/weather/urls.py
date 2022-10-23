from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_city', views.submit_city)
]