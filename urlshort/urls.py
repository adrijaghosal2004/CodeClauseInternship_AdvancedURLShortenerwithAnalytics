from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.shortenedUrl, name='create'),
    path('forward/<path:url>/', views.forward, name='forward')

]
