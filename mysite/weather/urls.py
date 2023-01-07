from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('city/', views.week_view, name="submit"),
    path('city/day/<int:pk>/<str:graph>', views.day_view),
]
