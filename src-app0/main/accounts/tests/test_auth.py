from django.test import TestCase
from django.contrib.auth.models import User
from ninja_jwt.tokens import AccessToken, RefreshToken
import json

class AuthenticationTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "password123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_token_obtain_pair(self):
        # Ninja JWT default controller is at root of api if not prefixed
        # In api.py we registered NinjaJWTDefaultController
        # By default it seems to put them at /token/pair etc relative to api root
        # We moved mount point to /api/auth/
        response = self.client.post(
            '/api/auth/token/pair',
            data=json.dumps({'username': self.username, 'password': self.password}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('access', data)
        self.assertIn('refresh', data)

    def test_token_verify(self):
        token = AccessToken.for_user(self.user)
        response = self.client.post(
            '/api/auth/token/verify',
            data=json.dumps({'token': str(token)}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
