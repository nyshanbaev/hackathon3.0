from django.shortcuts import render
from rest_framework import generics
from applications.musics.models import Song
from applications.musics.serializers import SongSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    pagination_class = CustomPagination
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'category']
    search_fields = ['title']



class SongCreateAPIView(generics.CreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


    
class SongUpdateAPIView(generics.UpdateAPIView):
    queryset = Song.objects.all() 
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]



class SongDeleteAPIView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = Song 



class SongDetailAPIView(generics.RetrieveAPIView): 
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'


    
    


