from rest_framework import serializers, status
from rareapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')