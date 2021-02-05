from django.db import models
from django.urls import path
from .views import *
from django.views.generic.detail import DetailView
from .models import Photo
# 2차 URL 파일
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    
]