from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='imagelist'),
    path('uploadimage', views.upload_image, name='uploadimage'),
    path('updateimage/<int:pk>/', views.update_image, name='updateimage'),
]