from django.http import HttpResponse


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
