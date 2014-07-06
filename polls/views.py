from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Choice, Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = dict(latest_poll_list=latest_poll_list)
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = dict(poll=poll)
    return render(request, 'polls/detail.html', context)


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = dict(poll=poll)
    return render(request, 'polls/results.html', context)


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = dict(poll=poll, error_message="You didn't select a choice.")
        # Redisplay the poll voting form
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
