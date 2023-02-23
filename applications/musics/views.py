from django.shortcuts import render
from rest_framework import generics
from applications.musics.models import Song
from applications.feedback.models import Rating, Like, Dislike
from applications.musics.serializers import SongSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from applications.musics.permissions import IsOwner


class CustomPagination(PageNumberPagination):
    page_size = 5
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
    permission_classes = [IsAuthenticated, IsOwner]



class SongDeleteAPIView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = Song 
    permission_classes = [IsAuthenticated, IsOwner]




class SongDetailAPIView(generics.RetrieveAPIView): 
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'

    
    # @action(methods=['POST'], detail=True)
    # def like(self, request, pk, *args, **kwargs):
    #     user = request.user
    #     like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
    #     like_obj.is_like = not like_obj.is_like
    #     like_obj.save()
    #     status = 'liked'

    #     if not like_obj.is_like:
    #         status = 'like_undo'

    #     return Response({'status': status})

    # @action(methods=['POST'], detail=True)
    # def like(self, request, pk, *args, **kwargs):
    #     user = request.user
    #     dislike_obj, _ = Dislike.objects.get_or_create(owner=user, post_id=pk)
    #     dislike_obj.is_like = not dislike_obj.is_dislike
    #     dislike_obj.save()
    #     status = 'dislike'

    #     if not dislike_obj.is_like:
    #         status = 'dislike_undo!'

    #     return Response({'status': status})    

    
    


