from rest_framework import serializers
from .models import Article, News, Company_data

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id", "title", "category", "date", "text", "image")

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ("id", "title", "category", "date", "text", "image")

class Company_dataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company_data
        fields = ("id", "name", "category", "image", "pr", "ceo", "tell", "point", "area1", "area2", "price", "address", "year", "cledit", "homepage", "staff", "pay", "security", "cancel")