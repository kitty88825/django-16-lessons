import random

from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render

from .models import Product


def about(request):
    quotes = [
        '今日事，今日畢',
        '要怎麼收穫，先那麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運',
    ]
    quotes = random.choice(quotes)

    return render(request, 'about.html', locals())


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>中古機列表</title>
    </head>
    <body>
        <h2>以下是目前本店販售中的二手機列表</h2>
        <hr>
        <table width=400 border=1 bgcolor="#CCFFCC">
        {}
        </table>
    </body>
    </html>
    '''

    products = Product.objects.all()
    tags = '<tr><td>品名</td><td>售價</td><td>大小</td></tr>'
    for p in products:
        tags = tags + f'<tr><td>{p.name}</td>'
        tags = tags + f'<td>{p.price}</td>'
        tags = tags + f'<td>{p.size}</td></tr>'

    return HttpResponse(html.format(tags))


def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    return render(request, 'disp.html', locals())
