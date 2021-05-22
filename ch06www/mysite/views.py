from datetime import datetime

from django.shortcuts import render


def index(request, tvno=0):
    now = datetime.now()
    tv_list = [
        {'name': '李榮浩《不遺憾》', 'tvcode': 'VR0Cl19hTTU'},
        {'name': '徐子未《慢冷》', 'tvcode': 'KD6MG3YXPDo'},
        {'name': '魏宏宇《Tom&Jerry》', 'tvcode': 'Bl6kIYBBnJA'},
    ]
    tvno = tvno
    tv = tv_list[tvno]

    return render(request, 'index.html', locals())
