import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

from django.urls import reverse
class QuestionModelTest(TestCase):

    def test_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_question1(self):
        time = timezone.now() - datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() +datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTest(TestCase):
    def test_view_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "НЕТ ВОПРОСОВ!")
        self.assertQuerysetEqual(response.context['latest.question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question>'])

    def test_future_question(self):
        create_question(question_text="Future question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Нет вопросов!")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        create_question(question_text="Past question", days = 30)
        create_question(question_text="Future question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['Latest_question_list'], ['<Question: Past question>'])

    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days = 30)
        create_question(question_text="Past question 2.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 1.'])

class QuestionViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question", days = 5)
        url = reverse('polls:detail', args=[future_question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
            past_question = create_question(question_text="Past question", days = 5)
            url = reverse('polls:detail', args=[past_question.id])
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)