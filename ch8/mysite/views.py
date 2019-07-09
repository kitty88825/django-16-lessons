from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None # 不要學書上打null

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False
    return render(request, 'index.html', locals())
