from django.core.mail import EmailMessage
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Diary, Mood, Post, Profile
from .form import ContactForm, DiaryForm, LoginForm, ProfileForm


@login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = User.objects.get(username=username)
            diaries = Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass

    messages.get_messages(request)

    return render(request, 'index.html', locals())


def listing(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()

    return render(request, 'listing.html', locals())


@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email

    messages.get_messages(request)

    if request.method == 'POST':
        user = User.objects.get(username=username)
        diary = Diary(user=user)
        post_form = DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            post_form.save()
            messages.add_message(request, messages.INFO, '日記已儲存')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, '如要張貼訊息，則每一個欄位都要填...')
    else:
        post_form = DiaryForm()
        messages.add_message(request, messages.INFO, '如要張貼訊息，則每一個欄位都要填...')

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


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    else:
        login_form = LoginForm()

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, '成功登出了')

    return redirect('/')


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username

    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = Profile(user=user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.INFO, '個人資料已儲存')
            return HttpResponseRedirect('/userinfo')
        else:
            messages.add_message(request, messages.INFO, '要修改個人資料，每一個欄位都要填...')
    else:
        profile_form = ProfileForm()

    return render(request, 'userinfo.html', locals())
