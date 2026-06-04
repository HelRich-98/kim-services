from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('histoire/', views.story, name='story'),
    path('realisations/', views.gallery, name='gallery'),
]
