from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.conf import settings
from mysite import models, forms
import urllib, json

# Create your views here.
def index(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_email = request.session['user_email']
    return render(request, 'index.html', locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_mood = request.GET['mood']
        user_post = request.GET['user_post']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填呦！'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存！請記得你的編輯密碼[{}]！，訊息須經審查後才會顯示。'.format(user_pass)
    return render(request, 'posting.html', locals())


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感謝您的來信。'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            send_title = "來自【來自不吐不快】網站的網友意見"
            send_body = f'網友姓名：{user_name}\n 居住城市：{user_city}\n 是否在學：{user_school}\n 反應意見：如下{user_message}'
            send_mail(
                    send_title,
                    send_body,
                    settings.EMAIL_HOST_USER,
                    [user_email],
                    fail_silently=False,
                    )
        else:
            message = '請檢查您輸入的資訊是否正確！'
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['user_name'].strip()
            login_password = request.POST['password']
            try:
                user = models.User.objects.get(name=login_name)
                print(user)
                if user.password == login_password:
                    request.session['user_name'] = user.name
                    request.session['user_email'] = user.email
                    return redirect('/')
                else:
                    message = '密碼錯誤，請再檢查一次！'
            except:
                message = '找不到使用者'
        else:
            message = '請檢查輸入的欄位內容'
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())

def logout(request):
    if 'user_name' in request.session:
        Session.objects.all().delete()
        return redirect('/login/')
    return redirect('/')
    
def userinfo(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
    else:
        return redirect('/login/')

    try:
        userinfo = models.User.objects.get(name=user_name)
    except:
        pass
    return render(request, 'userinfo.html', locals())