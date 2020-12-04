from django.test import TestCase
from django.test import Client
import json
from django.contrib.auth.models import User

URL = 'https://nextar.flip.id'
URL_LOCAL = 'http://localhost:8000'
USER = 'HyzioY7LP6ZoO7nTYKbG8O4ISkyWnX1JvAEVAhtWKZumooCzqp41'
USERNAME = 'myuser'
PASS = '123'

class APITestCase(TestCase):
    def test_update_disburse(self):
        """The index page loads properly"""
        # response = self.client.post(path='http://localhost:8000/api/token/', data=login_param, content_type="application/json")
        User.objects.create_superuser(USERNAME, 'myemail@test.com', PASS)
        body = {
            'username': USERNAME,
            'password': PASS
        }
        response = self.client.post("/api/token/", \
                            data=json.dumps(body), \
                                content_type='application/json')
        token = response.json()['access']
        param = {
            'url':'/disburse', 
            'user':USER, 
            'passwd':'', 
            'bank_code':'0001', 
            'account_number':'000000000000', 
            'amount':3000000,
            'remark': 'test'
        }
        response = self.client.post('/disbursement/disburse', \
                        data=json.dumps(param), \
                            content_type='application/json', \
                                HTTP_AUTHORIZATION='Bearer {}'.format(token))
        response = self.client.put('/disbursement/disburse/{}'.format(response.json()['message']['id']), \
                            content_type='application/json', \
                                HTTP_AUTHORIZATION='Bearer {}'.format(token))
        self.assertEqual(response.status_code, 200)

    def test_create_disburse(self):
        """The index page loads properly"""
        # response = self.client.post(path='http://localhost:8000/api/token/', data=login_param, content_type="application/json")
        User.objects.create_superuser(USERNAME, 'myemail@test.com', PASS)
        body = {
            'username': USERNAME,
            'password': PASS
        }
        response = self.client.post("/api/token/", \
                            data=json.dumps(body), \
                                content_type='application/json')
        param = {
            'url':'/disburse', 
            'user':USER, 
            'passwd':'', 
            'bank_code':'0001', 
            'account_number':'000000000000', 
            'amount':3000000,
            'remark': 'test'
        }
        response = self.client.post('/disbursement/disburse', \
                        data=json.dumps(param), \
                            content_type='application/json', \
                                HTTP_AUTHORIZATION='Bearer {}'.format(response.json()['access']))
        self.assertEqual(response.status_code, 200)