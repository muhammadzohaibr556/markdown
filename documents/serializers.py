from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class DocumentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created', 'updated', 'tags']


class DocumentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'content', 'tags']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']