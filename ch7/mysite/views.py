from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', locals())


def detail(reqest, id):
    try:
        product = models.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(reqest, 'detail.html', locals())