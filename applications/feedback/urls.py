from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import FeedbackModelViewSet

router = DefaultRouter()
router.register('', FeedbackModelViewSet)


urlpatterns = [
    path('feedback/', include(router.urls))

]