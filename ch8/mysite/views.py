from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()

    return render(request, 'index.html', locals())