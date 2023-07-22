from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('download/', views.download_file, name='download'),
]
