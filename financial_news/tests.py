from django.test import TestCase, Client
from django.urls import reverse
from .models import News

class NewsModelTest(TestCase):
    def setUp(self):
        News.objects.create(
            title='Test title',
            content='Test content',
            author='Test author',
            publish_date='2023-05-15'
        )

    def test_news_content(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.title}'
        self.assertEqual(expected_object_name, 'Test title')

class NewsViewTest(TestCase):
    def setUp(self):
        News.objects.create(
            title='Test title',
            content='Test content',
            author='Test author',
            publish_date='2023-05-15'
        )

    def test_news_list_view(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'news_list.html')
