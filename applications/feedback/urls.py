from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import *

router = DefaultRouter()
router.register('', LikeModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
