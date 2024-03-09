import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTest(TestCase):

    def test_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_question1(self):
        time = timezone.now() - datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)