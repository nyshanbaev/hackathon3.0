from django.urls import path, include
from applications.musics.views import *

urlpatterns = [
    path('', SongListAPIView.as_view()),
    path('create/', SongCreateAPIView.as_view()),
    path('update/<int:pk>/', SongUpdateAPIView.as_view()),
    path('delete/<int:pk>/', SongDeleteAPIView.as_view()),
    path('detail/<int:id>/', SongDetailAPIView.as_view()),

]