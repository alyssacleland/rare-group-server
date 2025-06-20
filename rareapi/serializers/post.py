from rest_framework import serializers
from ..models.post import Post, User, Category
from .user import UserSerializer
from .category import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = '__all__'