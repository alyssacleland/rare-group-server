"""View module for handling requests about events"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rareapi.models import Tag
from rareapi.serializers import TagSerialzier
from rest_framework import status


class TagView(ViewSet):
    """rareapi tags view"""

# RETRIEVE SINGLE TAG
    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerialzier(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# LIST ALL TAGS

# CREATE A TAG

# EDIT A TAG

# DELETE A TAG


# Add and remove tag from post logic should be in post view? (similar to join and le in levlup!)
