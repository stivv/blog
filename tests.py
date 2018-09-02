import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date = timezone.now()+datetime.timedelta(days=30))
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(pub_date = timezone.now() - datetime.timedelta(days=1,seconds=1))
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59))
        self.assertIs(recent_question.was_published_recently(), True)
