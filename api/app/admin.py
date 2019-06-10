from django.contrib import admin
from .models import Article, News, Company_data

admin.site.register(Article)
admin.site.register(News)
admin.site.register(Company_data)
