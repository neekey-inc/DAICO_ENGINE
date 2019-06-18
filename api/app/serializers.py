from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id", "uuid", "title", "category", "publish_start_at", "detail", "file", "deleted", "created_at", "modified_at")

