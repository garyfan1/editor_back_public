from django.shortcuts import render
from rest_framework import viewsets, filters
from editor.models import Post, Tag, Category
from editor.serializer import PostSerializer, UserSerializer, TagSerializer, CategorySerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

# import sqlite3
# Create your views here.
# print(f"version: {sqlite3.sqlite_version}")


class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'editor_text', 'tags__tag_name']
    filterset_fields = ['title', 'editor_text']

    def get_queryset(self):
        print(self.request.user.id)
        return Post.objects.filter(user=self.request.user.id)
        # return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



