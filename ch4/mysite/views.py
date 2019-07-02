from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product

# Create your views here.

def about(request):
    html='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>歡迎來到我的 ch4 痛苦王國</title>
    </head>
    <body>
        <h1>痛苦痛苦王國</h1>
        <hr>
        這裡很痛苦
    </body>
    </html>
    '''
    return HttpResponse(html)


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>中古機列表</title>
    </head>
    <body>
        <h2>以下是目前本店販售中的二手機列表</h2>
        <hr>
        <table width=400 border=1 bgcolor=#ccffcc>
            {}
        </table>
    </body>
    </html>
    '''
    product = Product.objects.all()
    tags = '<tr><td>品名</td><td>售價</td><td>大小</td></tr>'
    for p in product:
        tags = tags+ '<tr><td>{}</td>'.format(p.name)
        tags = tags+ '<td>{}</td>'.format(p.price)
        tags = tags+ '<td>{}</td></tr>'.format(p.size)

    return HttpResponse(html.format(tags))


def disp_detail(request, sku):
    html='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{0}</title>
    </head>
    <body>
        <h2>{1}</h2>
        <hr>
        <table width=400 border=1 bgcolor=#ccffcc>{2}</table>
        <a href="/list">回列表</a>
    </body>
    </html>
    '''
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    tags = '<tr><td>品項編號</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>品項名稱</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>二手售價</td><td>{}</td></tr>'.format(p.price)
    tags = tags + '<tr><td>尺寸大小</td><td>{}</td></tr>'.format(p.size)

    return HttpResponse(html.format(p.name, p.name, tags))