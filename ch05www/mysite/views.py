from django.http import HttpResponse
from django.urls import reverse
from django.urls.conf import path


def homepage(request, testmode):
    year = 2021
    month = 5
    day = 21
    postid = 1
    html = f"<a href={reverse('post-url', args=(year, month, day, postid))}>Show the Post</a>"

    return HttpResponse(html)


def about(request, author_no=0):
    html = f"<h2>Here is Author: {author_no}'s about page!</h2><hr>"

    return HttpResponse(html)

def listing(request, list_date):
    html = f'<h2>List Date is {list_date}</h2><hr>'

    return HttpResponse(html)

def post(request, yr, mon, day, post_num):
    html = f'<h2>{yr}/{mon}/{day}: Post Number: {int(post_num)}</h2><hr>'

    return HttpResponse(html)
