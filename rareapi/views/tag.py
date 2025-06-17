"""View module for handling requests about events"""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rareapi.models import Tag
from rareapi.serializers import TagSerializer
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
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# LIST ALL TAGS

    def list(self, request):
        """ handle requests to GET all tags

              Returns:
                  Response -- JSON serialized tag
        """

        tags = Tag.objects.all()

        # filter tags by post if we want
        post = request.query_params.get('post', None)
        if post is not None:
            tags = tags.filter(post_id=post)

        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

# CREATE A TAG

    def create(self, request):
        """handle POST operations for tags
        Returns:
        Response -- JSON serialized tag instance"""
        tag = Tag.objects.create(
            label=request.data["label"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)


# EDIT A TAG

    def update(self, request, pk):
        """ Handle PUT requests for a tag
        Returns:
        Response-- empty body with 204 status code"""
        tag = Tag.objects.get(pk=pk)
        tag.label = request.data["label"]
        tag.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

# DELETE A TAG

    def destroy(self, request, pk):
        """ Handle DELETE requests for a tag
        Returns:
        Response-- empty body with 204 status code"""
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# Add and remove tag from post logic should be in post view? (similar to join and le in levlup!)
