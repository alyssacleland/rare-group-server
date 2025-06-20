from rest_framework import serializers
from ..models.post import Post, User, Category
from .user import UserSerializer
from .category import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
