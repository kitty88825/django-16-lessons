from django.shortcuts import render

from .models import Mood, Post


def index(request, pid=None, del_pass=None):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'

    if del_pass and pid:
        try:
            post = Post.objects.get(id=pid)
        except:
            post = None

        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = '資料刪除成功'
            else:
                message = '密碼錯誤'
    elif user_id != None:
        mood = Mood.objects.get(status=user_mood)
        post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = f'成功儲存！請記得你的編輯密碼[{user_pass}]!訊息須經審查後才會顯示。'

    return render(request, 'index.html', locals())
