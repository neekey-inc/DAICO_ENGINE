

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path("", include(router.urls))
]