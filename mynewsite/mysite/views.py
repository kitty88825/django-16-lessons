from django.http import HttpResponse
from django.http.response import Http404

from .models import Product


def about(request):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Myself</title>
    </head>
    <body>
        <h2>Xin-Cen Xie</h2>
        <hr>

        <p>Hi, I am Xin-Cen Xie. Nice to meet you!</p>
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
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{}</title>
    </head>
    <body>
        <h2>{}</h2>
        <hr>
        <table width=400 border=1 bgcolor="#CCFFCC">
        {}
        </table>
        <a href="/list">回列表</a>
    </body>
    </html>
    '''
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    tags = f'<tr><td>品項編號</td><td>{p.sku}</td></tr>'
    tags = tags + f'<tr><td>品項名稱</td><td>{p.name}</td></tr>'
    tags = tags + f'<tr><td>二手售價</td><td>{p.price}</td></tr>'
    tags = tags + f'<tr><td>大小</td><td>{p.size}</td></tr>'

    return HttpResponse(html.format(p.name, p.name, tags))
