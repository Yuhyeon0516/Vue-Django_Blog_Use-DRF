from django.contrib.auth.models import User
from rest_framework import viewsets

from api2.serializer import PostSerializer, UserSerializer
from blog.models import Post


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
