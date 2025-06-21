from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rareapi.models import PostTag
from rareapi.serializers import PostTagSerializer

class PostTagView(ViewSet):

    def retrieve(self, request, pk):
        try:
            post_tag = PostTag.objects.get(pk=pk)
            serializer = PostTagSerializer(post_tag)
            return Response(serializer.data)
        except PostTag.DoesNotExist:
            return Response({"message": "PostTag not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        post_tags = PostTag.objects.all()

        # Optional filtering
        post_id = request.query_params.get('post_id')
        tag_id = request.query_params.get('tag_id')
        if post_id:
            post_tags = post_tags.filter(post__id=post_id)
        if tag_id:
            post_tags = post_tags.filter(tag__id=tag_id)

        serializer = PostTagSerializer(post_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            post_tag = PostTag.objects.get(pk=pk)
            serializer = PostTagSerializer(post_tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PostTag.DoesNotExist:
            return Response({"message": "PostTag not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            post_tag = PostTag.objects.get(pk=pk)
            post_tag.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PostTag.DoesNotExist:
            return Response({"message": "PostTag not found"}, status=status.HTTP_404_NOT_FOUND)
