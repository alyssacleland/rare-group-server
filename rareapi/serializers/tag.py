from rest_framework import serializers, status
from rareapi.models import Tag


class TagSerialzier(serializers.ModelSerializer):
    """JSON serializer for tags"""

    class Meta:
        model = Tag
        fields = ('id', 'label')
