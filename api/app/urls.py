

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, NewsViewSet, Company_dataViewSet

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'news', NewsViewSet)
router.register(r'company_data', Company_dataViewSet)

urlpatterns = [
    path("", include(router.urls))
]