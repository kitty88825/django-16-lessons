from django.shortcuts import render

from .models import Mood, Post


def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()

    return render(request, 'index.html', locals())
