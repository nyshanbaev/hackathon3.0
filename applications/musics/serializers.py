from rest_framework import serializers
from applications.musics.models import *
from applications.feedback.serializers import LikeSerializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = AuthorSerializer(instance.images.all(), many=True, context=self.context).data

        return representation

class SongSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = '__all__'


class SongImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongImage
        fields = '__all__'
        
        def _get_image_url(self, obj):
            if obj.image:
                url = obj.image.url
                request = self.context.get('request')
                if request is not None:
                    url = request.build_absolute_uri(url)
                else:
                    url = ''
                    return url

        def to_representation(self, instance):
            representation = super().to_representation(instance)  
            representation['images'] = self._get_image_url(instance)   
            return representation     

class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'