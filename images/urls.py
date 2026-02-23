from django.urls import path
from . import views

urlpatterns = [
    path('imagelist', views.image_list, name='imagelist'),
]