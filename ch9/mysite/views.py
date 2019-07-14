from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from mysite import models, forms
import urllib, json

# Create your views here.
def index(request, pid=None, del_pass=None):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message = 'cookie supported'
    else:
        message = 'cookie not supported'
    request.session.set_test_cookie()

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


def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                message = '您的訊息已儲存。要等管理者啟用後才看得到喔。'
                post_form.save() # form表單儲存進入資料庫
                return HttpResponseRedirect('/list')
            else:
                message = 'reCAPTCHA驗證失敗，請再確認'
        else:
            message = '如要張貼訊息，則每一個欄位都要填！'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填！！'
    return render(request, 'post2db.html', locals())