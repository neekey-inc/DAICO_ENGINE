from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, NewsSerializer
from .models import Article, News

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

