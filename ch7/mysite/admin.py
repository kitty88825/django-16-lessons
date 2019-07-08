from django.contrib import admin
# from mysite.models import Maker, PModel, Product, PPhoto
from mysite import models

# Register your models here.
# 另一種import方法
# admin.site.register(Maker)
# admin.site.register(PModel)
# admin.site.register(Product)
# admin.site.register(PPhoto)

admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product)
admin.site.register(models.PPhoto)
