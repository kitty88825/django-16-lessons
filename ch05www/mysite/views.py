from django.http import HttpResponse
from django.urls.conf import path


def homepage(request):
    return HttpResponse('Hello World!')


def about(request, author_no):
    html = f"<h2>Here is Author: {author_no}'s about page!</h2><hr>"

    return HttpResponse(html)

def listing(request, list_date):
    html = f'<h2>List Date is {list_date}</h2><hr>'

    return HttpResponse(html)

def post(request, yr, mon, day, post_num):
    html = f'<h2>{yr}/{mon}/{day}: Post Number: {int(post_num)}</h2><hr>'

    return HttpResponse(html)
