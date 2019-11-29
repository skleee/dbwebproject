from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(primary_key=True) #pk이다
    pimg = models.ImageField() #이미지
    brand = models.CharField(max_length=20) #브랜드이름
    category = models.CharField(max_length=20) #카테고리
    price = models.IntegerField() #가격
    pname = models.CharField(max_length=20) #제품명
    stock = models.IntegerField(default = 0) #현재 수량
    stocksold = models.IntegerField(default=0) #팔린 수량 (누적으로 기록)
    pub_date = models.DateField('product registered', default = timezone.now)
    def __str__(self):
        return self.pname
