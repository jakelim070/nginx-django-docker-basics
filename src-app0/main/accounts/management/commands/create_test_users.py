from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates test users'

    def handle(self, *args, **options):
        users = [
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
        ]

        for user_data in users:
            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create_user(**user_data)
                self.stdout.write(self.style.SUCCESS(f"Created user {user_data['username']}"))
            else:
                self.stdout.write(self.style.WARNING(f"User {user_data['username']} already exists"))
