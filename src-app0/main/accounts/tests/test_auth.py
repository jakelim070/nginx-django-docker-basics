from django.test import TestCase
from django.contrib.auth.models import User
import json
from ..utils import decode_token

class AuthenticationTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "password123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({'username': self.username, 'password': self.password}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('access', data)
        self.assertIn('refresh', data)

        # Verify token content
        decoded = decode_token(data['access'])
        self.assertEqual(decoded['username'], self.username)
        self.assertEqual(decoded['type'], 'access')

    def test_login_invalid(self):
        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({'username': self.username, 'password': 'wrongpassword'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 401)
