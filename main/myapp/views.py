from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    
    for count, post in enumerate(posts):
        post_lists.append("No.{}：".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" + str(post.body + "</small><br><br>"))
    return HttpResponse(post_lists)