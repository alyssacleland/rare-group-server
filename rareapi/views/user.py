from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User

class UserView(ViewSet):

# GET REQUEST FOR A SINGLE USER
  def retrieve(self, request, pk):
      user = User.objects.get(pk=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)

# GET REQUEST FOR USERS
  def list(self, request):
    users = User.objects.all()
    userId = request.query_params.get('uid', None)
    if userId is not None:
      users = users.filter(uid=userId)

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# POST REQUEST FOR USERS
  def create(self, request):
    user = User.objects.create(
      first_name=request.data["first_name"],
      last_name=request.data["last_name"],
      bio=request.data["bio"],
      profile_image_url=request.data["profile_image_url"],
      email=request.data["email"],
      created_on=request.data["created_on"],
      active=request.data["active"],
      is_staff=request.data["is_staff"],
      uid=request.data["uid"]
    )
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# PUT REQUEST FOR USERS
  def update(self, request, pk):
    id = pk
    user = User.objects.get(pk=pk)
    user.first_name=request.data["first_name"]
    user.last_name=request.data["last_name"]
    user.bio=request.data["bio"]
    user.profile_image_url=request.data["profile_image_url"]
    user.email=request.data["email"]
    user.created_on=request.data["created_on"]
    user.active=request.data["active"]
    user.is_staff=request.data["is_staff"]
    user.uid=request.data["uid"]

    user.save()

    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def destroy(self, request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')