from rest_framework import serializers
from .models import Article, News

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id", "title", "category", "date", "text", "image")

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ("id", "title", "category", "date", "text", "image")