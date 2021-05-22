from django.http import HttpResponse

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
