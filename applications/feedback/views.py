from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from applications.feedback.serializers import *
from applications.musics.models import Song
from applications.musics.permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from applications.musics.views import CustomPagination
from rest_framework.permissions import IsAuthenticated

class FeedbackModelViewSet(ModelViewSet):
    queryset = Feedback.objects.all()  
    serializer_class = FeedbackSerializer 
  

    
    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)   

    # def get_queryset(self):
    #     queryset = super().get_queryset()  
    #     queryset = queryset.filter(owner=self.request.user)
    #     return queryset                 

# class FeedbackViewSet(ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer
#     permission_classes = [IsOwner]

#     pagination_class = CustomPagination

#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['owner', 'title']
#     search_fields = ['title'] 
#     ordering_fields = ['id', 'owner']

    
    

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

    # @action(methods=['POST'], detail=True) 
    # def rating(self, request, pk, *args, **kwargs):
    #     serializer = RatingSerializer(data=request.data)  
    #     serializer.is_valid(raise_exception=True)  
    #     rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
    #     rating_obj.rating = request.data['rating']
    #     rating_obj.save()
    #     return Response(serializer.data)

    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)