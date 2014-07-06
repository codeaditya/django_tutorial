import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll


def create_poll(question, days):
    """
    Creates a poll with the given `question` published the given number
    of `days` offset to now (negative for polls published in the past,
    positive for polls that have yet to be published).
    """
    return Poll.objects.create(
        question=question,
        pub_date=timezone.now() + datetime.timedelta(days=days)
    )


class PollMethodTest(TestCase):

    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future.
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertFalse(future_poll.was_published_recently())

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is older than 1 day.
        """
        old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertFalse(old_poll.was_published_recently())

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently() should return True for polls whose
        pub_date is within the last day.
        """
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertTrue(recent_poll.was_published_recently())
