from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def detail(request, poll_id):
    return HttpResponse("You are looking at Poll {id}".format(id=poll_id))


def results(request, poll_id):
    return HttpResponse("You are looking at the results of Poll {id}"
                        "".format(id=poll_id))


def vote(request, poll_id):
    return HttpResponse("You are voting on Poll {id}".format(id=poll_id))
