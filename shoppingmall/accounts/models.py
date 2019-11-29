from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#구매자
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #유저모델과 1:1 연결
    is_buyer = models.BooleanField(default = False) #구매자의 경우 True
    is_seller = models.BooleanField(default = False) #판매자의 경우 True
    pids = models.ManyToManyField(to='shop.Product')  #"Product"의 아이디와 M:N 연결
    address = models.TextField(max_length=100) #주소 필드
    
    def __str__(self):
        return self.user.username

#판매자
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)  #유저모델과 1:1 연결
    is_buyer = models.BooleanField(default = False) #구매자의 경우 True
    is_seller = models.BooleanField(default = False)#판매자의 경우 True
    def __str__(self):
        return self.user.username