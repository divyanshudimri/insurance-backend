from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.customer_1 = User.objects.create(
            first_name='Divyanshu', last_name='Dimri',
            username='dimri@div',
            date_of_birth=(timezone.now() - timedelta(days=28 * 365)).date()
        )
        self.customer_2 = User.objects.create(
            first_name='Sudhanshu', last_name='Dimri',
            username='sud@dimri',
            date_of_birth=(timezone.now() - timedelta(days=40 * 365)).date()
        )
        self.list_url = reverse('v1:customer-list')

    def test_user_creation(self) -> None:
        payload = {
            'first_name': 'David',
            'last_name': 'Goggins',
            'date_of_birth': '1992-04-10',
            'username': 'dgog'
        }
        res = self.client.post(self.list_url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=payload['username'])
        self.assertEqual(user.first_name, 'David')
        self.assertEqual(user.last_name, 'Goggins')

    def test_user_search(self):
        res = self.client.get(self.list_url, data={'search': 'tes'})
        self.assertEqual(len(res.json()['results']), 0)

        res = self.client.get(self.list_url, data={'search': 'Dim'})
        self.assertEqual(len(res.json()['results']), 2)

        res = self.client.get(self.list_url, data={'search': 'Div'})
        self.assertEqual(len(res.json()['results']), 1)

    def test_user_date_of_birth_filter(self):
        res = self.client.get(self.list_url, data={'date_of_birth': '1995-12-27'})
        self.assertEqual(len(res.json()['results']), 1)
        self.assertEqual(res.json()['results'][0]['username'], self.customer_1.username)
