from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from applications.feedback.serializers import *
from applications.musics.models import Song
from applications.musics.permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from applications.musics.views import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class LikeModelViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        print(user)
        like_obj, _ = Like.objects.get_or_create(owner=user,id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        if not like_obj.is_like:
            status = 'unliked'
        return Response({'status': status})