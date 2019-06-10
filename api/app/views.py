from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, NewsSerializer, Company_dataSerializer
from .models import Article, News, Company_data

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

class Company_dataViewSet(viewsets.ModelViewSet):
    serializer_class = Company_dataSerializer
    queryset = Company_data.objects.all()

