from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rareapi.models.post import Post, User, Category
from rareapi.serializers import PostSerializer


class PostView(ViewSet):

    # GET /posts/:id/
    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    # GET /posts/ & FILTER /posts?tag=:id
    def list(self, request):
        posts = Post.objects.all()
        tag_id = request.query_params.get('tag', None)
        if tag_id is not None:
            posts = posts.filter(post_tags__tag_id=tag_id)
        user_uid = request.query_params.get('user_uid', None)
        if user_uid is not None:
            posts = posts.filter(user__uid=user_uid)
        is_public = request.query_params.get('public', None)
        if is_public is not None:
            is_public_bool = is_public.lower() == 'true'
            posts = posts.filter(is_public=is_public_bool)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # POST /posts/

    def create(self, request):

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT /posts/:id/
    def update(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE /posts/:id/
    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
