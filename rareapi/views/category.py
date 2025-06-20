from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rareapi.models import Category
from rareapi.serializers import CategorySerializer

class CategoryView(ViewSet):

    # GET SINGLE CATEGORY
    def retrieve(self, request, pk=None):
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

    # GET CATEGORIES
    def list(self, request):
        categories = Category.objects.all().order_by('label')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)