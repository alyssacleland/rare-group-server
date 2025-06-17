from rest_framework import serializers
from ..models.postTag import PostTag

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'
