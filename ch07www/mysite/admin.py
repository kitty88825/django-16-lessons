from django.contrib import admin

from .models import Maker, PModel, PPhoto, Product


admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(Product)
admin.site.register(PPhoto)
