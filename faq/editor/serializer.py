from editor.models import Post, Tag, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True, source="category.name")
    # tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "user", "editor_text", "tags", "category"]


class TagSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        # fields = '__all__'
        fields = ['id', 'tag_name', 'posts']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', "name", "posts"]

