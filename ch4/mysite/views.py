from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def about(request):
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
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in product:
        tags = tags+ '<tr><td>{}</td>'.format(p.name)
        tags = tags+ '<td>{}</td>'.format(p.price)
        tags = tags+ '<td>{}</td></tr>'.format(p.size)

    return HttpResponse(html.format(tags))


def listing(request):
    pass