from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, BlogPostSubscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BlogPostSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSubscription
        fields = '__all__'

