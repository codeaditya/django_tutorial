from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, dict(
        latest_poll_list=latest_poll_list,
    ))
    return HttpResponse(template.render(context))


def detail(request, poll_id):
    return HttpResponse("You are looking at Poll {id}".format(id=poll_id))


def results(request, poll_id):
    return HttpResponse("You are looking at the results of Poll {id}"
                        "".format(id=poll_id))


def vote(request, poll_id):
    return HttpResponse("You are voting on Poll {id}".format(id=poll_id))
