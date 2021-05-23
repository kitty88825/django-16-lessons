from django.shortcuts import render


def index(request):
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False

    return render(request, 'index.html', locals())
