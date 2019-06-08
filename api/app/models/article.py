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
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=4)
    published_at = models.DateField()
    detail = models.TextField()
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.title
