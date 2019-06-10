import uuid
from django.db import models
from django.utils import timezone

class Company_data(models.Model):
    class Meta:
        db_table = 'company_data'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/')
    pr = models.CharField(max_length=50)
    ceo = models.CharField(max_length=30)
    tell = models.CharField(max_length=15)
    point = models.CharField(max_length=100)
    area1 = models.CharField(max_length=10)
    area2 = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    cledit = models.CharField(max_length=20)
    homepage = models.URLField(max_length=100)
    staff = models.CharField(max_length=10)
    service = models.TextField()
    pay = models.TextField()
    cancel = models.TextField() 
    security = models.TextField()
    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.name