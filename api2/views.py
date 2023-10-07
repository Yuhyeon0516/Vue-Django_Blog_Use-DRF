# from django.contrib.auth.models import User
# from rest_framework import viewsets

# from api2.serializer import CommentSerializer, PostSerializer, UserSerializer
# from blog.models import Comment, Post


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from api2.serializer import CommentSerializer, PostSerializer

from blog.models import Comment, Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
