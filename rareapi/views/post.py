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
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # POST /posts/

    def create(self, request):
        userId = User.objects.get(pk=request.data["user_id"])
        category = Category.objects.get(pk=request.data["category_id"])
        post = Post.objects.create(
        user=userId,
        category=category,
        title=request.data["title"],
        publication_date=request.data["publication_date"],
        image_url=request.data["image_url"],
        content=request.data["content"],
    )
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
