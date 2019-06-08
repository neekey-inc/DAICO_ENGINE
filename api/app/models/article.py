from django.db import models
from django.utils import timezone
from sqlalchemy import Column, Index, ForeignKey, Sequence, func
from sqlalchemy import String, Text, Boolean, Integer, Float, BigInteger, Date
from sqlalchemy.orm import relationship, backref
# from app.config import config
import uuid
import datetime

class Article(models.Model):
    class Meta:
        db_table = 'article'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='media/')
    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.title
