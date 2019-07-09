from django.db import models

# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10) # 廠商名稱
    country = models.CharField(max_length=10) # 廠商所屬國家

    def __str__(self):
        return self.name

class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE) # 製造商名稱
    name = models.TextField(max_length=20) # 款式名稱
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png') # 規格網址

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE) # 手機規格
    nickname = models.CharField(max_length=15, default='超值二手機') # 簡單說明
    description = models.TextField(default='暫無說明') # 詳細說明
    year = models.PositiveIntegerField(default=2016) # 製造年份(正整數)
    price = models.PositiveIntegerField(default=0) # 售價(正整數)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # 產品名稱
    description = models.TextField(max_length=20,default='產品照片') # 照片內容
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png') # 照片網址

    def __str__(self):
        return self.description




