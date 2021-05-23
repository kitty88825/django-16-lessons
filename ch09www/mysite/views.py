from django.core.mail import EmailMessage
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Mood, Post
from .form import ContactForm, LoginForm, PostForm


def index(request):
    if 'username' in request.session:
        username = request.session['username']
        usercolor = request.session['usercolor']

    return render(request, 'index.html', locals())


def listing(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()

    return render(request, 'listing.html', locals())


def posting(request):
    moods = Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'

    if user_id != None:
        mood = Mood.objects.get(status=user_mood)
        post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = f'成功儲存！請記得你的編輯密碼[{user_pass}]!訊息須經審查後才會顯示。'

    return render(request, 'posting.html', locals())


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        message = '感謝您的來信。'
        user_name = form.cleaned_data['user_name']
        user_city = form.cleaned_data['user_city']
        user_school = form.cleaned_data['user_school']
        user_email = form.cleaned_data['user_email']
        user_message = form.cleaned_data['user_message']

        mail_body = u'''
        網友姓名：{}
        居住城市：{}
        是否在學：{}
        反映意見：如下
        {}
        '''.format(user_name, user_city, user_school, user_message)

        email = EmailMessage('來自【不吐不快】網站的網友意見', mail_body, user_email, [user_email])
        email.send()
    else:
        message = '請檢查您輸入的資訊是否正確！'

    return render(request, 'contact.html', locals())


def post2db(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            message = '您的訊息已儲存，要等管理者啟用後才看得到喔。'
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'

    return render(request, 'post2db.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['user_name']
            usercolor = request.POST['user_color']
            message = '登入成功'
        else:
            message = '請檢查輸入的欄位內容'
    else:
        login_form = LoginForm()

    try:
        if 'username' in request.session:
            request.session['username'] = username
        if 'usercolor' in request.session:
            request.session['usercolor'] = usercolor
    except:
        pass

    return render(request, 'login.html', locals())

def logout(request):
    request.session['username'] = None

    return redirect('/')
