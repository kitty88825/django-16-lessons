from django.shortcuts import redirect, render

from .models import Poll, PollItem


def index(request):
    polls = Poll.objects.all()
    return render(request, 'index.html', locals())


def poll(request, pollid):
    try:
        poll = Poll.objects.get(id=pollid)
    except:
        poll = None

    if poll:
        pollitems = PollItem.objects.filter(poll=poll).order_by('-vote')

    return render(request, 'poll.html', locals())


def vote(request, pollid, pollitemid):
    try:
        pollitem = PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None

    if pollitem:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()

    target_url = f'/poll/{pollid}'

    return redirect(target_url)
