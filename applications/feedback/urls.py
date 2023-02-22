from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import FeedbackViewSet

router = DefaultRouter()
router.register('', FeedbackViewSet)


urlpatterns = [
    path('feedback/', include(router.urls))

]