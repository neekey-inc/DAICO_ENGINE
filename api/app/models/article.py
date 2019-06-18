from django.db import models
from django.utils import timezone
import uuid

class Article(models.Model):
    class Meta:
        db_table = 'article'

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    detail = models.TextField()
    file = models.ImageField(upload_to='media/', null=True)
    publish_start_at = models.DateField()
    
    deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.title

