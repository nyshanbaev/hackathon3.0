from rest_framework import serializers
from applications.feedback.models import *

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = 'all'


class DislikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dislike
        fields = 'all'      

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Rating
        fields = ('rating',)   


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = 'all'


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('feedback',)